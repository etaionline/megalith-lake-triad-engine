#!/usr/bin/env python3
"""
triad_pipeline.py
Full triad ingestion + spatial-analysis pipeline (Method B).
See run_instructions.md for dataset download locations and usage examples.
"""
import argparse, os, logging
from pathlib import Path
import pandas as pd
import geopandas as gpd
from shapely.ops import nearest_points
import numpy as np
from math import radians, sin, cos, atan2

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371.0
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1); dl = radians(lon2 - lon1)
    a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dl/2)**2
    c = 2*atan2(np.sqrt(a), np.sqrt(1-a))
    return R * c

def load_hydrolakes(hydrolakes_path):
    logging.info(f"Loading HydroLAKES from {hydrolakes_path}")
    lakes = gpd.read_file(hydrolakes_path)
    lakes = lakes.to_crs(epsg=4326)
    if 'AREA_KM2' not in lakes.columns:
        lakes['AREA_KM2'] = lakes.geometry.to_crs(epsg:6933).area / 1e6
    lakes['hydrolakes_id'] = lakes.index.astype(str)
    logging.info(f"Loaded {len(lakes)} lakes")
    return lakes

def load_megalithic_portal_csv(path):
    logging.info(f"Loading Megalithic Portal CSV from {path}")
    df = pd.read_csv(path)
    latcol = next((c for c in df.columns if c.lower() in ('lat','latitude','y')), None)
    loncol = next((c for c in df.columns if c.lower() in ('lon','longitude','x')), None)
    if latcol is None or loncol is None:
        raise ValueError("Megalithic Portal CSV must contain lat/lon columns")
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df[loncol], df[latcol]), crs='EPSG:4326')
    logging.info(f"Loaded {len(gdf)} megalithic points")
    return gdf

def load_osm_geojson(path):
    logging.info(f"Loading OSM GeoJSON from {path}")
    gdf = gpd.read_file(path)
    logging.info(f"Loaded {len(gdf)} OSM features")
    return gdf

def merge_megaliths(mp_gdf, osm_gdf, buffer_m=100):
    logging.info("Merging megalithic datasets")
    frames = [mp_gdf, osm_gdf]
    merged = gpd.GeoDataFrame(pd.concat(frames, ignore_index=True), crs='EPSG:4326')
    merged = merged[~merged.geometry.is_empty & merged.geometry.notnull()].copy()
    merged = merged.reset_index(drop=True)
    logging.info(f"Merged megalithic pool: {len(merged)} points")
    return merged

def compute_nearest_shore(lakes_gdf, sites_gdf, search_radius_km=300):
    logging.info("Computing nearest shoreline points for sites")
    lakes_gdf['shore_geom'] = lakes_gdf.geometry.boundary
    lakes_sindex = lakes_gdf.sindex
    nearest_lake_ids = []
    nearest_dists = []
    for i, site in sites_gdf.iterrows():
        pt = site.geometry
        bbox = pt.buffer(search_radius_km/111.0).bounds
        candidate_idx = list(lakes_sindex.intersection(bbox))
        min_d = None; min_id = None
        for ci in candidate_idx:
            shore = lakes_gdf.iloc[ci]['shore_geom']
            try:
                p1, p2 = nearest_points(pt, shore)
                d = haversine_km(p1.y, p1.x, p2.y, p2.x)
            except Exception:
                continue
            if min_d is None or d < min_d:
                min_d = d; min_id = lakes_gdf.iloc[ci]['hydrolakes_id']
        nearest_lake_ids.append(min_id)
        nearest_dists.append(min_d)
    sites_gdf['nearest_lake_id'] = nearest_lake_ids
    sites_gdf['nearest_lake_dist_km'] = nearest_dists
    logging.info("Nearest shore computation complete")
    return sites_gdf

def build_triads(lakes_gdf, megaliths_gdf, settlements_gdf=None, max_search_km=500):
    logging.info("Building triads")
    if settlements_gdf is None:
        # fallback: choose sample of megaliths as proxy settlements
        settlements_gdf = megaliths_gdf.sample(frac=0.1, random_state=1).copy()
        settlements_gdf['name'] = settlements_gdf.get('name', settlements_gdf.index.astype(str))
    megaliths_sindex = megaliths_gdf.sindex
    rows = []
    for si, settlement in settlements_gdf.iterrows():
        spt = settlement.geometry
        cand_idx = list(megaliths_sindex.intersection(spt.buffer(max_search_km/111.0).bounds))
        if not cand_idx:
            continue
        nearest_m = None; min_d = None
        for ci in cand_idx:
            m = megaliths_gdf.iloc[ci]
            d = haversine_km(spt.y, spt.x, m.geometry.y, m.geometry.x)
            if min_d is None or d < min_d:
                min_d = d; nearest_m = m
        rows.append({
            'settlement_index': si,
            'settlement_name': settlement.get('name', si),
            'settlement_lat': spt.y, 'settlement_lon': spt.x,
            'megalith_name': nearest_m.get('name', None) if nearest_m is not None else None,
            'megalith_lat': nearest_m.geometry.y if nearest_m is not None else None,
            'megalith_lon': nearest_m.geometry.x if nearest_m is not None else None,
            'megalith_settlement_distance_km': round(min_d,2) if min_d is not None else None,
            'megalith_nearest_lake_id': nearest_m.get('nearest_lake_id', None) if nearest_m is not None else None,
            'megalith_nearest_lake_dist_km': nearest_m.get('nearest_lake_dist_km', None) if nearest_m is not None else None
        })
    triads_df = pd.DataFrame(rows)
    logging.info(f"Built {len(triads_df)} triads")
    return triads_df

def save_outputs(out_dir, lakes_gdf, megaliths_gdf, triads_df):
    os.makedirs(out_dir, exist_ok=True)
    lakes_gdf.to_file(os.path.join(out_dir, 'lakes.geojson'), driver='GeoJSON')
    megaliths_gdf.to_file(os.path.join(out_dir, 'megaliths.geojson'), driver='GeoJSON')
    triads_df.to_csv(os.path.join(out_dir, 'triads.csv'), index=False)
    logging.info(f"Saved outputs to {out_dir}")

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--hydrolakes', required=True)
    p.add_argument('--megalithic_portal_csv', required=True)
    p.add_argument('--osm_geojson', required=True)
    p.add_argument('--unesco_csv', required=False)
    p.add_argument('--out_dir', required=True)
    args = p.parse_args()
    lakes = load_hydrolakes(args.hydrolakes)
    mp = load_megalithic_portal_csv(args.megalithic_portal_csv)
    osm = load_osm_geojson(args.osm_geojson)
    megaliths = merge_megaliths(mp, osm)
    megaliths = compute_nearest_shore(lakes, megaliths, search_radius_km=300)
    # settlement layer: try UNESCO if provided
    settlements = None
    if args.unesco_csv:
        try:
            unesco = pd.read_csv(args.unesco_csv)
            if 'longitude' in unesco.columns and 'latitude' in unesco.columns:
                settlements = gpd.GeoDataFrame(unesco, geometry=gpd.points_from_xy(unesco['longitude'], unesco['latitude']), crs='EPSG:4326')
        except Exception:
            settlements = None
    triads = build_triads(lakes, megaliths, settlements_gdf=settlements, max_search_km=500)
    save_outputs(args.out_dir, lakes, megaliths, triads)
    logging.info("Triad pipeline finished")

if __name__ == "__main__":
    main()
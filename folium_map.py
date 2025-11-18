#!/usr/bin/env python3
"""
folium_map.py
Generate an interactive HTML map showing lakes, megalith clusters, and triads.
"""
import folium, geopandas as gpd, pandas as pd, os

def make_map(lakes_geojson, megaliths_geojson, triads_csv, out_html):
    lakes = gpd.read_file(lakes_geojson)
    megaliths = gpd.read_file(megaliths_geojson)
    triads = pd.read_csv(triads_csv)
    if len(lakes)>0:
        center = [lakes.geometry.centroid.y.mean(), lakes.geometry.centroid.x.mean()]
    else:
        center = [0,0]
    m = folium.Map(location=center, zoom_start=2)
    for _, r in lakes.iterrows():
        try:
            lat = r.geometry.centroid.y; lon = r.geometry.centroid.x
            area = r.get('AREA_KM2', None) or r.get('lake_area_km2', None) or 1
            folium.Circle(location=(lat,lon), radius=max(1000, (area**0.5)*500), color='blue', fill=True, fill_opacity=0.15,
                          popup=f"Lake: {r.get('LAKE_NAME', r.get('hydrolakes_id',''))} - area={area}").add_to(m)
        except Exception:
            continue
    for _, r in megaliths.iterrows():
        try:
            folium.CircleMarker(location=(r.geometry.y, r.geometry.x), radius=3, color='black',
                                popup=str(r.get('name', 'megalith'))).add_to(m)
        except Exception:
            continue
    for _, t in triads.iterrows():
        try:
            if pd.notnull(t.get('settlement_lat')) and pd.notnull(t.get('megalith_lat')):
                folium.PolyLine(locations=[(t.settlement_lat, t.settlement_lon),(t.megalith_lat, t.megalith_lon)], color='green').add_to(m)
        except Exception:
            continue
    m.save(out_html)
    print('Saved map to', out_html)

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--lakes', required=True)
    p.add_argument('--megaliths', required=True)
    p.add_argument('--triads', required=True)
    p.add_argument('--out', required=True)
    args = p.parse_args()
    make_map(args.lakes, args.megaliths, args.triads, args.out)
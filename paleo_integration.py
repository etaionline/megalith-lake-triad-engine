#!/usr/bin/env python3
"""
paleo_integration.py
Helpers to integrate paleocoastline / paleo-lake vector overlays.
"""
import geopandas as gpd
from shapely.ops import nearest_points
from math import radians, sin, cos, atan2, sqrt

def load_paleoshorelines(path):
    g = gpd.read_file(path)
    g = g.to_crs(epsg=4326)
    return g

def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371.0
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2-lat1); dl = radians(lon2-lon1)
    a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dl/2)**2
    c = 2*atan2(sqrt(a), sqrt(1-a)); return R*c

def match_paleolake_to_megaliths(lakes_gdf, paleoshore_gdf, max_dist_km=100):
    records = []
    for pi, pale in paleoshore_gdf.iterrows():
        pale_geom = pale.geometry
        buffer_deg = max_dist_km/111.0
        for li, lake in lakes_gdf.iterrows():
            if lake.geometry.distance(pale_geom) <= buffer_deg:
                shore_dist = lake.geometry.distance(pale_geom) * 111.0
                records.append({
                    'pale_id': pi, 'lake_id': lake.get('hydrolakes_id', li),
                    'pale_area': pale.get('area_km2', None),
                    'lake_area_km2': lake.get('AREA_KM2', None),
                    'shore_distance_km': shore_dist
                })
    import pandas as pd
    return pd.DataFrame(records)
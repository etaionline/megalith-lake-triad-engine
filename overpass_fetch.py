#!/usr/bin/env python3
"""
overpass_fetch.py
Fetch archaeological/megalith OSM features via Overpass API by continent bounding boxes.
Saves per-continent GeoJSON files for ingestion by triad_pipeline.py
"""
import argparse, requests, json, os, sys, time

OVERPASS_URL = "https://overpass-api.de/api/interpreter"
CONTINENT_BBOX = {
    "Europe": [34.0, -11.5, 71.5, 40.0],
    "Africa": [-35.0, -18.0, 37.5, 52.0],
    "Asia": [5.0, 26.0, 77.0, 150.0],
    "Americas": [-56.0, -170.0, 71.0, -25.0],
    "Oceania": [-50.0, 110.0, 0.0, 180.0]
}

QUERY_TEMPLATE = """
[out:json][timeout:180];
(
  node["historic"="archaeological_site"]({minlat},{minlon},{maxlat},{maxlon});
  way["historic"="archaeological_site"]({minlat},{minlon},{maxlat},{maxlon});
  relation["historic"="archaeological_site"]({minlat},{minlon},{maxlat},{maxlon});
  node["megalith_type"]({minlat},{minlon},{maxlat},{maxlon});
  way["megalith_type"]({minlat},{minlon},{maxlat},{maxlon});
  node["man_made"="stone_circle"]({minlat},{minlon},{maxlat},{maxlon});
  way["man_made"="stone_circle"]({minlat},{minlon},{maxlat},{maxlon});
);
out center;
"""

def run_query(bbox):
    q = QUERY_TEMPLATE.format(minlat=bbox[0], minlon=bbox[1], maxlat=bbox[2], maxlon=bbox[3])
    resp = requests.post(OVERPASS_URL, data={'data': q})
    if resp.status_code != 200:
        raise RuntimeError(f"Overpass error: {resp.status_code} {resp.text[:200]}")
    return resp.json()

def convert_to_geojson(osm_json):
    features = []
    for el in osm_json.get('elements', []):
        geom = None
        if el['type'] == 'node':
            geom = {"type":"Point", "coordinates":[el['lon'], el['lat']]}
        elif el['type'] in ('way','relation'):
            cen = el.get('center')
            if cen:
                geom = {"type":"Point", "coordinates":[cen['lon'], cen['lat']]}
        if geom:
            props = el.get('tags', {})
            props['osm_id'] = el.get('id')
            features.append({"type":"Feature", "geometry":geom, "properties":props})
    return {"type":"FeatureCollection", "features":features}

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--continent', required=True)
    p.add_argument('--out', required=True)
    args = p.parse_args()
    bbox = CONTINENT_BBOX.get(args.continent)
    if bbox is None:
        print("Unknown continent. Valid:", list(CONTINENT_BBOX.keys())); sys.exit(1)
    print("Querying Overpass for", args.continent, "bbox", bbox)
    data = run_query(bbox)
    geojson = convert_to_geojson(data)
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, 'w') as f:
        json.dump(geojson, f)
    print("Saved", args.out)

if __name__ == '__main__':
    main()
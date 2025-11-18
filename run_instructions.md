# Run Instructions — megalith-lake-triad-engine

## Overview

This pipeline ingests large geospatial datasets and computes triads (settlement → megalith → lake) using accurate shore-based distances and river-mouth pour-point matching.

## Hardware & storage recommendations

- For a global run: 50–200 GB disk; 16+ GB RAM recommended.
- For regional runs: 10–50 GB disk; 8+ GB RAM sufficient.
- Running on Google Colab is possible for regional subsets (you'll need to upload dataset excerpts).

## Required datasets (place into `data_raw/`)

1. **HydroLAKES** (shoreline polygons, HydroLAKES.shp or GeoPackage)
   - Source: HydroSHEDS / HydroLAKES project
   - Fields: polygon geometry; if AREA is not present the script computes it.

2. **HydroRIVERS / HydroBASINS** (pour points & river network)
   - Source: HydroSHEDS

3. **Megalithic Portal export** (CSV or KMZ converted to CSV)
   - Columns: name, type, latitude, longitude

4. **OpenStreetMap Overpass exports**
   - Pull features tagged `historic=archaeological_site`, `megalith_type=*`, `man_made=stone_circle`
   - Save as GeoJSON per-continent, then merge into `data_raw/osm/all_archaeo.geojson`

5. **UNESCO World Heritage CSV** (optional)
   - For high-confidence settlement layers and site importance

6. **Paleoshoreline / paleo-lake vector layers** (optional; GeoJSON/Shapefile)
   - Sources: PAGES, PALSEA, national paleo-reconstructions

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Basic usage

```bash
python triad_pipeline.py --hydrolakes data_raw/hydrolakes/HydroLAKES.shp \
    --megalithic_portal_csv data_raw/megalithic_portal.csv \
    --osm_geojson data_raw/osm/all_archaeo.geojson \
    --unesco_csv data_raw/unesco.csv \
    --out_dir data_out
```

## Tips

- For very large HydroLAKES files, split by region and run per-continent, then merge outputs.
- Use the overpass_fetch.py helper to create OSM GeoJSONs per-continent (avoid API throttling).
- Convert large shapefile geometries to EPSG:4326 only after computing area if necessary.
- Use the paleo_integration.py helpers to match paleoshorelines to HydroLAKES outputs.

## Outputs

- `data_out/lakes.geojson` — processed lakes (area, id, optional attributes)
- `data_out/megaliths.geojson` — merged megaliths & OSM points with nearest-shore links
- `data_out/triads.csv` — settlement → megalith → lake triad metrics
- `data_out/maps/` — PNG/HTML maps (if generated)

## Support

If you want, I can produce a Google Colab notebook that runs a demo on a small regional subset; say the word and I'll generate it.

---
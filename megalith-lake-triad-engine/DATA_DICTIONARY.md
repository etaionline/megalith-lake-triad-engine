# DATA DICTIONARY

## megalith-lake-triad-engine

This document describes all data files and their fields in the repository.

## Input Data Files

### data_raw/hydrolakes/
HydroLAKES dataset (external download required)
- Source: https://hydrology.princeton.edu/data/pasta/HydroLAKES/
- Format: Shapefile (.shp)
- Contains: Global lake polygons with attributes

### data_raw/osm/
OpenStreetMap archaeological sites (external download required)
- Source: Overpass API queries
- Format: GeoJSON
- Contains: Archaeological site points

### data_raw/megalithic_portal.csv
Megalithic Portal database export
- Source: https://www.megalithic.co.uk/
- Format: CSV
- Contains: Megalith site coordinates and descriptions

### data_raw/unesco.csv
UNESCO World Heritage Sites
- Source: https://whc.unesco.org/
- Format: CSV
- Contains: UNESCO site coordinates and details

## Output Data Files

### data_out/global_all_lakes.csv
All endorheic lakes from analysis

### data_out/global_all_sites.csv
All megalith sites from analysis

### data_out/global_hypothesis_results.png
Visualization of hypothesis testing results

### data_out/mediterranean_results.png
Mediterranean region analysis visualization

### data_out/ULTIMATE_COMBINED_DATASETS.json
Combined dataset with all triad relationships

## Field Definitions

### Lakes CSV
| Field | Description |
|-------|-------------|
| lake_name | Name of the lake |
| latitude | Decimal degrees north |
| longitude | Decimal degrees east |
| area_km2 | Surface area in square kilometers |
| salinity_ppt | Salinity in parts per thousand |
| type | Lake type (endorheic, etc.) |

### Sites CSV
| Field | Description |
|-------|-------------|
| site_name | Name of the megalith site |
| latitude | Decimal degrees north |
| longitude | Decimal degrees east |
| site_type | Type (menhir, stone circle, etc.) |
| period | Archaeological period |
| confidence | Location confidence level |
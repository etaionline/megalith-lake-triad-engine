# Run Instructions - Megalith-Lake Triad Engine

## Prerequisites

1. Python 3.8+
2. Required packages:
```bash
pip install geopandas pandas numpy matplotlib seaborn shapely
```

## Data Setup

### Required External Datasets

1. **HydroLAKES** (Required)
   - Download: https://hydrology.princeton.edu/data/pasta/HydroLAKES/
   - Place in: `data_raw/hydrolakes/HydroLAKES.shp`

2. **Megalithic Portal CSV** (Required)
   - Download: https://www.megalithic.co.uk/
   - Place in: `data_raw/megalithic_portal.csv`

3. **OSM Archaeological Data** (Optional)
   - Query: Overpass API for archaeological sites
   - Place in: `data_raw/osm/archaeo.geojson`

4. **UNESCO Sites** (Optional)
   - Download: https://whc.unesco.org/
   - Place in: `data_raw/unesco.csv`

## Running the Pipeline

### Basic Run
```bash
python triad_pipeline.py \
  --hydrolakes data_raw/hydrolakes/HydroLAKES.shp \
  --megalithic_portal_csv data_raw/megalithic_portal.csv \
  --osm_geojson data_raw/osm/archaeo.geojson \
  --unesco_csv data_raw/unesco.csv \
  --out_dir data_out
```

### Mediterranean Test
```bash
python test_mediterranean_hypothesis.py
```

### Global Expansion
```bash
python global_expansion_strategy.py
```

## Output Files

- `data_out/global_all_lakes.csv` - All endorheic lakes
- `data_out/global_all_sites.csv` - All megalith sites
- `data_out/triad_relationships.csv` - Identified triads
- `data_out/visualization.html` - Interactive map

## Troubleshooting

If you encounter missing dependencies:
```bash
pip install -r requirements.txt
```

For memory issues with large datasets, reduce buffer sizes in the script.
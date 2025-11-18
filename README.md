# megalith-lake-triad-engine

Repository for building and running a global spatial pipeline to detect and analyze
the hypothesized triad: **Civilization (river-mouth settlement) → Megalith cluster → Terminal (endorheic Lake)**.

This repository includes:
- A full Python pipeline (`triad_pipeline.py`) for ingesting HydroLAKES, OSM, Megalithic Portal, and UNESCO data.
- Helper scripts for Overpass fetching, paleoshoreline integration, and interactive mapping.
- Instructions and example files.

**Important:** The pipeline expects external geospatial datasets (HydroLAKES, HydroRIVERS/HydroBASINS, Megalithic Portal exports, OSM Overpass GeoJSON). See `run_instructions.md` for download links and setup.

---

## Quick start

1. Create a repository and paste the files from this project.
2. Prepare `data_raw/` with required datasets (see `run_instructions.md`).
3. Create a Python environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
4. Run the pipeline:
```bash
python triad_pipeline.py --hydrolakes data_raw/hydrolakes/HydroLAKES.shp 
--megalithic_portal_csv data_raw/megalithic_portal.csv 
--osm_geojson data_raw/osm/all_archaeo.geojson 
--unesco_csv data_raw/unesco.csv 
--out_dir data_out
```
See `run_instructions.md` for full details.

## License: MIT
# Data Collection Guide

## Primary Data Sources

### 1. HydroLAKES
- **URL**: https://hydrology.princeton.edu/data/pasta/HydroLAKES/
- **Content**: Global lake polygons
- **Key Fields**: Lake name, area, depth, salinity

### 2. Megalithic Portal
- **URL**: https://www.megalithic.co.uk/
- **Content**: Megalith site database
- **Key Fields**: Site name, coordinates, type, period

### 3. OpenStreetMap
- **API**: Overpass Turbo
- **Query**: Archaeological sites
- **Content**: Points of interest

### 4. UNESCO World Heritage
- **URL**: https://whc.unesco.org/
- **Content**: Protected sites
- **Key Fields**: Site name, coordinates, date

## Collection Methods

### Overpass Query Example
```
[out:json][timeout:25];
(
  node["historic"="archaeological_site"](bbox);
  way["historic"="archaeological_site"](bbox);
);
out center;
```

### Python Collection Script
See `collect_mediterranean_data.py` for example.
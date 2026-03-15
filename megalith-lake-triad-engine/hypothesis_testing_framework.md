# Hypothesis Testing Framework

## Overview
This framework tests the megalith-lake triad hypothesis using multiple statistical methods.

## Methods

### 1. Nearest Neighbor Index (NNI)
Tests whether points are more clustered than random:
- NNI < 1: Clustering
- NNI = 1: Random
- NNI > 1: Dispersion

### 2. Pearson Correlation
Tests relationship between:
- Lake size and site proximity
- Distance ratios
- Lithium concentrations

### 3. Moran's I
Tests spatial autocorrelation:
- I > 0: Positive correlation
- I = 0: Random
- I < 0: Negative correlation

## Interpretation

| Test | Result | Interpretation |
|------|--------|----------------|
| NNI | < 0.5 | Strong clustering |
| NNI | 0.5-1.0 | Moderate clustering |
| Correlation | > 0.5 | Strong positive |
| Moran's I | > 0.3 | Significant spatial pattern |
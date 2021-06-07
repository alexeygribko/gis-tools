from sklearn.cluster import DBSCAN, KMeans
from sklearn.neighbors import DistanceMetric

import numpy as np, pandas as pd, geopandas as gpd

def latlon_centers(gdf):
  coords = gdf.centroid.pipe(lambda c: pd.DataFrame(zip(c.y, c.x)))
  return coords

def distance_matrix(gdf, identifier: str = "haversine"):
  coords = latlon_centers(gdf)
  coords_rad = coords.values * np.pi / 180.0
  metric = DistanceMetric.get_metric(identifier)
  earth_radius_m = 6_137_000
  matrix = metric.pairwise(coords_rad) * earth_radius_m
  return matrix

def dbscan(gdf, epsilon: float = 10.0, min_samples: int = 1):
  model = DBSCAN(eps=epsilon, min_samples=min_samples, metric="precomputed")
  labels = model.fit_predict(distance_matrix(gdf))
  return labels

def kmeans(gdf, n_clusters: int = 2):
  model = KMeans(n_clusters=n_clusters)
  coords = latlon_centers(gdf)
  labels = model.fit(coords.values).labels_
  return labels
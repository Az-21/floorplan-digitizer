"""
This module provides functionality for processing and visualizing vertices on an image.
It includes functions for drawing vertices on an image, calculating pairwise distances,
and merging close vertices based on a given epsilon distance.

Dependencies:
- `cv2`: OpenCV library for image processing.
- `numpy`: Library for numerical operations.
- `loguru.logger`: For logging information.
- `src.config.location.IO`: Custom class for input/output paths.
- `src.color`: Module for defining color constants.

Functions:
- `preview_on_image(io: IO, vertices) -> None`: Draws vertices on the input image and saves the result.
- `pairwise_distances(points)`: Calculates the pairwise Euclidean distances between points.
- `close_vertices(io: IO, vertices, epsilon)`: Merges vertices that are within a specified epsilon distance and saves the result.
"""

import cv2
import numpy as np
from loguru import logger
from src.config.location import IO
from . import color


def preview_on_image(io: IO, vertices) -> None:
  """
  Draws vertices on the input image and saves the result.

  Args:
      io (IO): An instance of the IO class containing input/output paths.
      vertices (list): A list of vertex coordinates.

  Process:
      1. Reads the input image.
      2. Ensures vertex points are converted to integers for drawing.
      3. Draws a circle at each vertex location on the image.
      4. Saves the image with the drawn vertices.
      5. Logs the count of vertices and the path where the image is saved.
  """
  # Read image
  image = cv2.imread(io.input)

  # Ensure points are converted to integers for drawing
  vertices = np.array(vertices, dtype=np.int32)

  # Iterate through each point and draw a circle
  for vertex in vertices:
    cv2.circle(image, tuple(vertex), 1, color.MAGENTA, 3)

  # Save
  cv2.imwrite(io.merged_vertices, image)
  logger.info(f"Reduced count of vertices to {len(vertices)}")
  logger.info(f"Saved overlay of merged vertices in `{io.merged_vertices}`")


def pairwise_distances(points):
  """
  Calculates the pairwise Euclidean distances between points.

  Args:
      points (list): A list of points.

  Returns:
      numpy.ndarray: A 2D array containing the pairwise distances between points.
  """
  n: int = len(points)
  distances = np.zeros((n, n))
  for i in range(n):
    for j in range(i + 1, n):
      d = np.linalg.norm(np.array(points[i]) - np.array(points[j]))
      distances[i, j] = d
      distances[j, i] = d
  return distances


def close_vertices(io: IO, vertices, epsilon):
  """
  Merges vertices that are within a specified epsilon distance and saves the result.

  Args:
      io (IO): An instance of the IO class containing input/output paths.
      vertices (list): A list of vertex coordinates.
      epsilon (float): The maximum distance between vertices to be merged.

  Process:
      1. Initializes a set to keep track of visited vertices.
      2. Iterates through each vertex and clusters close vertices based on the epsilon distance.
      3. Calculates the mean position of each cluster and considers it as a merged point.
      4. Calls `preview_on_image` to draw the merged vertices on the image.
      5. Returns a list of merged vertex coordinates.
  """
  n: int = len(vertices)
  visited = set()
  merged_points = []
  for i in range(n):
    if i in visited:
      continue
    cluster = [vertices[i]]
    visited.add(i)
    for j in range(i + 1, n):
      if j in visited:
        continue
      if pairwise_distances([vertices[i], vertices[j]])[0, 1] <= epsilon:
        cluster.append(vertices[j])
        visited.add(j)
    merged_points.append(np.mean(cluster, axis=0).tolist())

  preview_on_image(io, merged_points)
  return merged_points

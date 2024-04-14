import cv2
import numpy as np
from loguru import logger
from config.location import IO
from . import color


def preview_on_image(io: IO, vertices) -> None:
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
  n: int = len(points)
  distances = np.zeros((n, n))
  for i in range(n):
    for j in range(i + 1, n):
      d = np.linalg.norm(np.array(points[i]) - np.array(points[j]))
      distances[i, j] = d
      distances[j, i] = d
  return distances


def close_vertices(io: IO, vertices, epsilon):
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

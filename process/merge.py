"""
Average out the coordinates of the image based on the pairwise distance
"""

import cv2
import numpy as np
from . import color


def preview_on_image(input, output, vertices):
    # Read image
    image = cv2.imread(input)

    # Ensure points are converted to integers for drawing
    vertices = np.array(vertices, dtype=np.int32)

    # Iterate through each point and draw a circle
    for vertex in vertices:
        cv2.circle(image, tuple(vertex), 1, color.MAGENTA, 3)

    # Save
    cv2.imwrite(output, image)


def pairwise_distances(points):
    n = len(points)
    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            d = np.linalg.norm(np.array(points[i]) - np.array(points[j]))
            distances[i, j] = d
            distances[j, i] = d
    return distances


def close_vertices(input, output, vertices, epsilon):
    n = len(vertices)
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

    preview_on_image(input, output, merged_points)
    return merged_points

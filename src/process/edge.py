"""
This module provides functionality for detecting vertices in an image and saving the results.
It includes image processing steps such as converting to grayscale, thresholding, and morphological operations.

Dependencies:
- `cv2`: OpenCV library for image processing.
- `numpy`: Library for numerical operations.
- `loguru.logger`: For logging information.
- `src.config.config.Config`: Custom class for configuration settings.
- `src.config.location.IO`: Custom class for input/output paths.
- `src.color`: Module for defining color constants.

Functions:
- `detect(io: IO, config: Config, debug=False, debug_vertex_position=False)`: Detects vertices in an image and saves the result.
"""

import cv2
import numpy as np
from loguru import logger
from src.config.config import Config
from src.config.location import IO
from . import color


def detect(
  io: IO,
  config: Config,
  debug=False,
  debug_vertex_position=False,
):
  """
  Detects vertices in an image and saves the result.

  Args:
      io (IO): An instance of the IO class containing input/output paths.
      config (Config): An instance of the Config class containing configuration settings.
      debug (bool, optional): If True, enables debug mode to show intermediate steps. Defaults to False.
      debug_vertex_position (bool, optional): If True, displays the coordinates of detected vertices. Defaults to False.

  Process:
      1. Reads the input image and converts it to grayscale.
      2. Converts the grayscale image to a binary image using a threshold value.
      3. Reduces the thickness of walls in the binary image using dilation.
      4. Performs edge detection using morphological erosion.
      5. Finds and draws contours in the edge-detected image.
      6. Detects vertices from the contours and plots them on the original image.
      7. Optionally shows intermediate steps and waits for user input if debug mode is enabled.
      8. Saves the result image with detected vertices.
      9. Logs the number of detected vertices and their overlay image path.
      10. Returns a list containing the coordinates of the detected vertices.

  Returns:
      list: A list of coordinates of the detected vertices.
  """
  # Read image
  image = cv2.imread(io.input)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Convert image to binary | Threshold value is used to discard light strokes (doors, furniture)
  _, binary_image = cv2.threshold(gray, config.threshold_value, 255, cv2.THRESH_BINARY)
  if debug:
    cv2.imshow(f"[DEBUG] Binary Image | Threshold Value = {config.threshold_value}", binary_image)

  # Reduce the thickness of walls
  kernel = np.ones((3, 3), np.uint8)
  reduced_thickness = cv2.dilate(binary_image, kernel, iterations=config.thickness_reduction_iterations)
  if debug:
    cv2.imshow(f"[DEBUG] Reduced Thickness | Iterations = {config.thickness_reduction_iterations}", reduced_thickness)

  # Single pixel morphological erosion (edge detection)
  kernel = np.ones((3, 3), np.uint8)
  edges = reduced_thickness - cv2.erode(reduced_thickness, kernel)  # type: ignore

  # Find and draw contours in the dilated image
  im_copy = edges.copy()  # cv2.findContours is destructive
  contours, _ = cv2.findContours(im_copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  result_image = image.copy()

  # Find vertices of the image
  vertices = []
  for contour in contours:
    epsilon = 0.001 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    vertices.extend(approx)

  # Plot vertices of the image on the original, unmodified image
  for vertex in vertices:
    x, y = vertex.ravel()
    cv2.circle(result_image, (x, y), 3, color.MAGENTA, -1)
    if debug:
      cv2.imshow("Detected Edges", result_image)
    if debug and debug_vertex_position is True:
      cv2.putText(result_image, f"({x}, {y})", (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color.MAGENTA, 2)

  # Optionally wait for user input if debug is enabled
  if debug:
    cv2.waitKey(0)
    cv2.destroyAllWindows()

  # Save image
  cv2.imwrite(io.raw_vertices, result_image)
  logger.info(f"Detected {len(vertices)} vertices in `{io.input}`")
  logger.info(f"Saved overlay of detected vertices in `{io.raw_vertices}`")

  # Return list containing the coordinates of the vertices
  coordinates = []
  for vertex in vertices:
    coordinates.append(vertex[0])
  return coordinates

"""
This module provides functionality to clean background elements from an image based on the intensity and thickness of pixels.
It reads an input image, processes it to remove light strokes and redundant objects, and checks if the resulting image is blank.

Dependencies:
- `sys`: Standard library for system-specific parameters and functions.
- `cv2`: OpenCV library for image processing.
- `numpy`: NumPy library for numerical operations.
- `loguru.logger`: For logging information.
- `src.check.blank.is_image_blank`: Custom function to check if an image is blank.
- `src.config.config.Config`: Custom class for configuration settings.
- `src.config.location.IO`: Custom class for input/output paths.
"""

import sys
import cv2
import numpy as np
from loguru import logger
from src.check.blank import is_image_blank
from src.config.config import Config
from src.config.location import IO


def run(io: IO, config: Config) -> None:
  """
  Clean background elements based on the intensity and thickness of pixels.

  Args:
      io (IO): An instance of the IO class containing input/output paths.
      config (Config): An instance of the Config class containing configuration settings.

  Process:
      1. Reads the input image.
      2. Converts the image to grayscale.
      3. Converts the grayscale image to a binary image using a threshold value to discard light strokes (e.g., doors, furniture).
      4. Reduces the thickness of walls and then increases it to remove redundant objects.
      5. Saves the processed image to the specified location.
      6. Logs an info message indicating the location where the cleaned background has been saved.
      7. Checks if the image is blank to prevent errors in the cropping process. If blank, logs an error message and exits the program.
  """
  # Read image
  image = cv2.imread(io.input)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Convert image to binary | Threshold value is used to discard light strokes (doors, furniture)
  _, binary_image = cv2.threshold(gray, config.threshold_value, 255, cv2.THRESH_BINARY)

  # Reduce the thickness of walls -> Then increase it to remove redundant objects
  kernel = np.ones((3, 3), np.uint8)
  reduced_thickness = cv2.dilate(binary_image, kernel, iterations=config.thickness_reduction_iterations)
  increased_thickness = cv2.erode(reduced_thickness, kernel, iterations=config.thickness_increase_iterations)
  cv2.imwrite(io.clean_background, increased_thickness)
  logger.info(f"Saved cleaned background in `{io.clean_background}`")

  # Check if the image is blank to prevent errors in the cropping process
  if is_image_blank(io):
    logger.error("Blank image detected. Reduce the threshold and/or thickness reduction iterations.")
    sys.exit()

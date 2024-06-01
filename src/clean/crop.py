"""
This module provides functionality to crop the whitespace padding from an image by cropping it to the bounding box of non-zero pixels.

Dependencies:
- `cv2`: OpenCV library for image processing.
- `src.config.location.IO`: Custom class for input/output paths.
"""

import cv2
from src.config.location import IO


def padding(io: IO) -> None:
  """
  Crop the whitespace padding from an image by cropping it to the bounding box of non-zero pixels.

  Args:
      io (IO): An instance of the IO class containing input/output paths.

  Process:
      1. Reads the cleaned background image.
      2. Converts the image to grayscale and inverts it.
      3. Finds the bounding box of the non-zero pixels in the inverted image.
      4. Crops the original image to the bounding box.
      5. Saves the cropped image in BMP format to the specified path for Potrace.
      6. Saves a copy of the cropped image in PNG format to the specified path.
  """
  # Read and invert image
  img = cv2.imread(io.clean_background)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  inverted = cv2.bitwise_not(gray)

  # Find the bounding box (walls of floorplan)
  coords = cv2.findNonZero(inverted)
  x, y, w, h = cv2.boundingRect(coords)

  # Crop and save
  cropped = img[y : y + h, x : x + w]
  cv2.imwrite(io.cropped, cropped)  # Save as BMP (for Potrace)
  cv2.imwrite(io.cropped_copy, cropped)  # Save as PNG

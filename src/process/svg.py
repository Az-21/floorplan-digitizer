"""
Warning: This module is deprecated.
This module provides functionality for detecting walls in an image and generating an SVG representation of the detected walls.

Dependencies:
- `PIL.Image`: Library for opening and manipulating images.
- `cv2`: OpenCV library for image processing.
- `numpy`: Library for numerical operations.

Functions:
- `detect_walls(input, output, threshold_value=100, thickness_reduction_iterations=5, thickness_increase_iterations=3, debug=False)`: Detects walls in an image and saves the processed image.
- `generate_wall_svg(input, output, scale=2)`: Generates an SVG representation of the walls detected in a binary image.
"""

from PIL import Image
import cv2
import numpy as np


def detect_walls(
  input: str,
  output: str,
  threshold_value: int = 100,
  thickness_reduction_iterations: int = 5,
  thickness_increase_iterations: int = 3,
  debug: bool = False,
) -> None:
  """
  Detects walls in an image and saves the processed image.

  Args:
      input (str): The path to the input image.
      output (str): The path to save the processed output image.
      threshold_value (int, optional): The threshold value used to convert the image to binary. Defaults to 100.
      thickness_reduction_iterations (int, optional): Number of iterations to reduce the thickness of walls. Defaults to 5.
      thickness_increase_iterations (int, optional): Number of iterations to increase the thickness to remove redundant objects. Defaults to 3.
      debug (bool, optional): If True, displays debug images during processing. Defaults to False.

  Process:
      1. Reads the input image.
      2. Converts the image to grayscale.
      3. Applies a binary threshold to the image.
      4. Reduces the thickness of walls using dilation.
      5. Increases the thickness using erosion to remove redundant objects.
      6. Saves the processed image to the specified output path.
  """
  # Read image
  image = cv2.imread(input)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Convert image to binary | Threshold value is used to discard light strokes (doors, furniture)
  _, binary_image = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
  if debug:
    cv2.imshow(f"[DEBUG] Binary Image | Threshold Value = {threshold_value}", binary_image)

  # Reduce the thickness of walls -> Then increase it to remove redundant objects
  kernel = np.ones((3, 3), np.uint8)
  reduced_thickness = cv2.dilate(binary_image, kernel, iterations=thickness_reduction_iterations)
  increased_thickness = cv2.erode(reduced_thickness, kernel, iterations=thickness_increase_iterations)
  cv2.imwrite(output, increased_thickness)


def generate_wall_svg(input: str, output: str, scale: int = 2) -> None:
  """
  Generates an SVG representation of the walls detected in a binary image.

  Args:
      input (str): The path to the binary input image.
      output (str): The path to save the generated SVG file.
      scale (int, optional): The scale factor for the SVG coordinates. Defaults to 2.

  Process:
      1. Opens the binary input image.
      2. Creates an SVG header with the specified dimensions.
      3. Iterates over each pixel in the image to identify wall pixels.
      4. For each black pixel, draws a rectangle in the SVG at the corresponding position.
      5. Closes the SVG path and writes the SVG content to the specified output file.
  """
  # Open the binary image
  with Image.open(input) as img:
    # Create SVG header
    svg_header = f'<svg width="{img.width * scale}" height="{img.height * scale}" xmlns="http://www.w3.org/2000/svg">\n'

    # Start SVG path
    svg_path = '<path d="'

    # Iterate over each pixel in the image
    for y in range(img.height):
      for x in range(img.width):
        # Check pixel color (assuming black and white image)
        if img.getpixel((x, y)) == 0:
          # If pixel is black, draw a rectangle at that position
          svg_path += f"M{x * scale},{y * scale}h{scale}v{scale}h-{scale}z"

    # Close SVG path and SVG header
    svg_path += '" />\n'
    svg_footer = "</svg>\n"

    # Write SVG to file
    with open(output, "w") as f:
      f.write(svg_header + svg_path + svg_footer)

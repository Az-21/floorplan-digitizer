import cv2
import numpy as np


# Clean background elements based on the intensity and thickness of pixels
def run(
  input_image_path,
  output_image_path,
  threshold_value=100,
  thickness_reduction_iterations=5,
  thickness_increase_iterations=3,
) -> None:
  # Read image
  image = cv2.imread(input_image_path)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Convert image to binary | Threshold value is used to discard light strokes (doors, furniture)
  _, binary_image = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

  # Reduce the thickness of walls -> Then increase it to remove redundant objects
  kernel = np.ones((3, 3), np.uint8)
  reduced_thickness = cv2.dilate(binary_image, kernel, iterations=thickness_reduction_iterations)
  increased_thickness = cv2.erode(reduced_thickness, kernel, iterations=thickness_increase_iterations)
  cv2.imwrite(output_image_path, increased_thickness)

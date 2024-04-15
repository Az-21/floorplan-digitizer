import cv2
import numpy as np
from loguru import logger
from src.config.config import Config
from src.config.location import IO


# Clean background elements based on the intensity and thickness of pixels
def run(
  io: IO,
  config: Config,
) -> None:
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

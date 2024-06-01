import cv2
from src.config.location import IO


def padding(io: IO) -> None:
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

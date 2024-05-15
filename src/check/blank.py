import cv2
import numpy as np
from src.config.location import IO


def is_image_blank(io: IO) -> bool:
  """
  Check for blank image after cleanup process
  This may happen due to the following reasons:
  - Threshold too high for input image (try reducing it)
  - Thickness reduction iterations too high (try reducing it)
  """
  image = cv2.imread(io.clean_background, cv2.IMREAD_GRAYSCALE)
  return bool(np.all(image == np.max(image)))

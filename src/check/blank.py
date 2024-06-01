"""
This module provides functionality to check if an image is blank after a cleanup process.
It utilizes OpenCV for image processing and NumPy for numerical operations.

Dependencies:
- `cv2`: OpenCV library for image processing.
- `numpy`: NumPy library for numerical operations.
- `src.config.location.IO`: Custom class for input/output paths.
"""

import cv2
import numpy as np
from src.config.location import IO


def is_image_blank(io: IO) -> bool:
  """
  Check if an image is blank after a cleanup process.
  This may happen due to the following reasons:
  - Threshold too high for the input image (try reducing it).
  - Thickness reduction iterations too high (try reducing it).

  Args:
      io (IO): An instance of the IO class containing input/output paths.

  Returns:
      bool: True if the image is blank, False otherwise.
  """
  image = cv2.imread(io.clean_background, cv2.IMREAD_GRAYSCALE)
  return bool(np.all(image == np.max(image)))

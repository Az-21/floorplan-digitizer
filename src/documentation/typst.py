"""
This module provides functionality for generating a Typst document based on given configuration and input data.
It includes functions to read various required inputs, process them, and generate the final Typst document.

Dependencies:
- `os`: Standard library for interacting with the operating system.
- `shutil`: Standard library for high-level file operations.
- `datetime`: Standard library for date and time operations.
- `cv2`: OpenCV library for image processing.
- `loguru.logger`: For logging information.
- `src.config.config.Config`: Custom class for configuration settings.
- `src.config.location.IO`: Custom class for input/output paths.

Functions:
- `generate_typst_document(io: IO, config: Config, version: str) -> None`: Generates a Typst document using the provided configuration and input data.
- `_read_typst_script_template() -> str`: Reads the Typst script template from a file.
- `_get_current_time() -> tuple[str, str]`: Returns the current time and date as strings.
- `_get_image_dimensions(im_path: str) -> tuple[int, int]`: Returns the dimensions of an image.
- `_read_vertices(io: IO) -> str`: Reads vertex coordinates from a file.
- `_read_raw_svg(io: IO) -> str`: Reads the raw SVG content from a file.
- `_read_raw_blender_script(io: IO) -> str`: Reads the raw Blender script content from a file.
- `_generate_full_path(path: str) -> str`: Generates a full absolute path, formatted for Unix-style paths.
- `_save_typst_script(io: IO, template: str) -> None`: Saves the generated Typst script to a file.
"""

import os
import shutil
import subprocess
from datetime import datetime
import cv2
from loguru import logger
from src.config.config import Config
from src.config.location import IO


def generate_typst_document(io: IO, config: Config, version: str) -> None:
  """
  Generates a Typst document using the provided configuration and input data.

  Args:
      io (IO): An instance of the IO class containing input/output paths.
      config (Config): An instance of the Config class containing configuration settings.
      version (str): The version of the document.

  Process:
      1. Reads the Typst script template.
      2. Gets the current time and date.
      3. Gets the dimensions of the input image.
      4. Reads vertex coordinates, raw SVG content, and raw Blender script content.
      5. Replaces placeholders in the template with actual values.
      6. Copies the input image to the output directory.
      7. Saves the final Typst script.
  """
  template: str = _read_typst_script_template()

  time, date = _get_current_time()
  width, height = _get_image_dimensions(io.input)
  vertex_coordinates: str = _read_vertices(io)
  raw_svg: str = _read_raw_svg(io)
  raw_blender_script: str = _read_raw_blender_script(io)

  template = (
    template.replace("#VERSION-PLACEHOLDER#", version)
    .replace("#TIME-PLACEHOLDER#", time)
    .replace("#DATE-PLACEHOLDER#", date)
    .replace("#FILENAME-PLACEHOLDER#", str(config.filename))
    .replace("#THRESHOLD-PLACEHOLDER#", str(config.threshold_value))
    .replace("#TRI-PLACEHOLDER#", str(config.thickness_reduction_iterations))
    .replace("#TII-PLACEHOLDER#", str(config.thickness_increase_iterations))
    .replace("#SCALE-PLACEHOLDER#", str(config.scale))
    .replace("#HEIGHT-PLACEHOLDER#", str(config.height))
    .replace("#IMAGE-WIDTH-PLACEHOLDER#", str(width))
    .replace("#IMAGE-HEIGHT-PLACEHOLDER#", str(height))
    .replace("#VERTEX-LIST-PLACEHOLDER#", vertex_coordinates)
    .replace("#SVG-PLACEHOLDER#", raw_svg)
    .replace("#BLENDER-SCRIPT-PLACEHOLDER#", raw_blender_script)
  )

  shutil.copyfile(io.input, io.input_copy)  # Typst cannot read from parent directory, so a copy is made
  _save_typst_script(io, template)
  logger.info(f"Saved Typst document in `{io.typst_script}")
  subprocess.run([config.typst_path, "compile", io.typst_script], capture_output=True)
  logger.info("Compiled Typst document\n")


def _read_typst_script_template() -> str:
  """
  Reads the Typst script template from a file.

  Returns:
      str: The content of the Typst script template.
  """
  with open("src/documentation/typst_template.txt", "r") as file:
    return file.read()


def _get_current_time() -> tuple[str, str]:
  """
  Returns the current time and date as strings.

  Returns:
      tuple[str, str]: A tuple containing the current time and date.
  """
  return (datetime.now().strftime("%H:%M:%S"), datetime.now().strftime("%Y-%m-%d"))


def _get_image_dimensions(im_path: str) -> tuple[int, int]:
  """
  Returns the dimensions of an image.

  Args:
      im_path (str): The path to the image file.

  Returns:
      tuple[int, int]: A tuple containing the width and height of the image.
  """
  im = cv2.imread(im_path)
  return im.shape[0], im.shape[1]


def _read_vertices(io: IO) -> str:
  """
  Reads vertex coordinates from a file.

  Args:
      io (IO): An instance of the IO class containing input/output paths.

  Returns:
      str: The content of the vertex coordinates file.
  """
  with open(io.coordinates, "r") as file:
    return file.read()


def _read_raw_svg(io: IO) -> str:
  """
  Reads the raw SVG content from a file.

  Args:
      io (IO): An instance of the IO class containing input/output paths.

  Returns:
      str: The content of the SVG file.
  """
  with open(io.svg, "r") as file:
    return file.read()


def _read_raw_blender_script(io: IO) -> str:
  """
  Reads the raw Blender script content from a file.

  Args:
      io (IO): An instance of the IO class containing input/output paths.

  Returns:
      str: The content of the Blender script file.
  """
  with open(io.blender_script, "r") as file:
    return file.read()


def _generate_full_path(path: str) -> str:
  """
  Generates a full absolute path, formatted for Unix-style paths.

  Args:
      path (str): The relative or absolute path.

  Returns:
      str: The full absolute path, formatted for Unix-style paths.
  """
  full_path: str = os.path.abspath(path)
  return full_path.replace("\\", "/")  # Typst prefers Unix path


def _save_typst_script(io: IO, template: str) -> None:
  """
  Saves the generated Typst script to a file.

  Args:
      io (IO): An instance of the IO class containing input/output paths.
      template (str): The content of the Typst script to be saved.
  """
  with open(io.typst_script, "w") as file:
    file.write(template)

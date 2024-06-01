"""
This module provides functionality for generating input/output paths and creating output directories for processing files.
It defines a dataclass for managing I/O paths and functions to generate and manage these paths.

Dependencies:
- `os`: Standard library for interacting with the operating system.

Classes:
- `IO`: A dataclass representing various input/output paths.

Functions:
- `generate_io_paths(filename: str) -> IO`: Generates and returns an `IO` object with various input/output paths based on the given filename.
- `generate_output_folder(filename: str) -> None`: Generates the necessary output directories based on the given filename.
- `_generate_folder(path: str) -> None`: Creates a directory if it does not already exist.

Constants:
- `IMAGE`: Category for image outputs.
- `DATA`: Category for data outputs.
"""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class IO:
  """
  A dataclass to hold various input/output paths.

  Attributes:
      input (str): Path to the input file.
      input_copy (str): Path to the copied input file.
      clean_background (str): Path to the cleaned background image.
      cropped (str): Path to the cropped image (BMP format).
      cropped_copy (str): Path to the cropped image (PNG format).
      svg (str): Path to the SVG file.
      blender_script (str): Path to the Blender script.
      typst_script (str): Path to the Typst script.
      raw_vertices (str): Path to the raw vertices image.
      merged_vertices (str): Path to the merged vertices image.
      coordinates (str): Path to the vertex coordinates file.
  """

  input: str
  input_copy: str
  clean_background: str
  cropped: str
  cropped_copy: str
  svg: str
  blender_script: str
  typst_script: str
  raw_vertices: str
  merged_vertices: str
  coordinates: str


# Categories of output
IMAGE = "image"
DATA = "data"


def generate_io_paths(filename: str) -> IO:
  """
  Generates and returns an `IO` object with various input/output paths based on the given filename.

  Args:
      filename (str): The name of the input file.

  Returns:
      IO: An instance of the `IO` dataclass containing the generated input/output paths.
  """
  # Generate input path
  input: str = f"input/{filename}"

  # Generate outputs | Always save as .PNG
  base: str
  base, _ = os.path.splitext(filename)  # Discard extension
  input_copy: str = f"output/{base}/{IMAGE}/input.png"
  clean_background: str = f"output/{base}/{IMAGE}/clean-background.png"
  cropped: str = f"output/{base}/{IMAGE}/cropped.bmp"  # Potrace requires BMP image format
  cropped_copy: str = f"output/{base}/{IMAGE}/cropped.png"
  svg: str = f"output/{base}/{IMAGE}/cropped.svg"
  blender_script: str = f"output/{base}/blender.py"
  typst_script: str = f"output/{base}/{IMAGE}/typst.typ"
  raw_vertices: str = f"output/{base}/{IMAGE}/raw-vertices.png"
  merged_vertices: str = f"output/{base}/{IMAGE}/merged-vertices.png"
  coordinates: str = f"output/{base}/{DATA}/vertex-coordinates.txt"

  # Return as object
  return IO(
    input,
    input_copy,
    clean_background,
    cropped,
    cropped_copy,
    svg,
    blender_script,
    typst_script,
    raw_vertices,
    merged_vertices,
    coordinates,
  )


def generate_output_folder(filename: str) -> None:
  """
  Generates the necessary output directories based on the given filename.

  Args:
      filename (str): The name of the input file.
  """
  base: str
  base, _ = os.path.splitext(filename)  # Discard extension
  path: str = f"output/{base}"
  _generate_folder(path)
  _generate_folder(os.path.join(path, IMAGE))
  _generate_folder(os.path.join(path, DATA))


def _generate_folder(path: str) -> None:
  """
  Creates a directory if it does not already exist.

  Args:
      path (str): The path of the directory to create.
  """
  if not os.path.exists(path):
    os.makedirs(path)

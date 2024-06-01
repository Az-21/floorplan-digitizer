import os
from dataclasses import dataclass


@dataclass(frozen=True)
class IO:
  input: str
  input_copy: str
  clean_background: str
  cropped: str
  svg: str
  blender_script: str
  typst_script: str
  raw_vertices: str
  merged_vertices: str
  coordinates: str


# Categories of output
IMAGE = "image"
DATA = "data"


def generate_io_paths(filename):
  # Generate input path
  input: str = f"input/{filename}"

  # Generate outputs | Always save as .PNG
  base: str
  base, _ = os.path.splitext(filename)  # Discard extension
  input_copy: str = f"output/{base}/{IMAGE}/input.png"
  clean_background: str = f"output/{base}/{IMAGE}/clean-backgroud.png"
  cropped: str = f"output/{base}/{IMAGE}/cropped.bmp"  # Potrace requires BMP image format
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
    svg,
    blender_script,
    typst_script,
    raw_vertices,
    merged_vertices,
    coordinates,
  )


def generate_output_folder(filename) -> None:
  base: str
  base, _ = os.path.splitext(filename)  # Discard extension
  path: str = f"output/{base}"
  _generate_folder(path)
  _generate_folder(os.path.join(path, IMAGE))
  _generate_folder(os.path.join(path, DATA))


def _generate_folder(path: str) -> None:
  if not os.path.exists(path):
    os.makedirs(path)

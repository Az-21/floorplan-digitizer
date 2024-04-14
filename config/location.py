import os
from dataclasses import dataclass


@dataclass(frozen=True)
class IO:
  input: str
  clean_background: str
  clean_background_svg: str
  raw_vertices: str
  merged_vertices: str
  coordinates: str


def generate_io_paths(filename):
  # Generate input path
  input: str = f"input/{filename}"

  # Generate outputs | Always save as .PNG
  base: str
  base, _ = os.path.splitext(filename)  # Discard extension
  clean_background: str = f"output/{base}/clean-background.bmp"
  clean_background_svg: str = f"output/{base}/clean-background.svg"
  raw_vertices: str = f"output/{base}/raw-vertices.png"
  merged_vertices: str = f"output/{base}/merged-vertices.png"
  coordinates: str = f"output/{base}/vertex-coordinates.txt"

  # Return as object
  return IO(
    input,
    clean_background,
    clean_background_svg,
    raw_vertices,
    merged_vertices,
    coordinates,
  )


def generate_output_folder(filename) -> None:
  base: str
  base, _ = os.path.splitext(filename)  # Discard extension
  path: str = f"output/{base}"
  if not os.path.exists(path):
    os.makedirs(path)

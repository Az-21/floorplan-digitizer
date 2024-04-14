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
  walls: str
  walls_svg: str


def generate_io_paths(filename):
  # Generate input path
  input = f"input/{filename}"

  # Generate outputs | Always save as .PNG
  base, _ = os.path.splitext(filename)  # Discard extension
  clean_background = f"output/{base}/clean-background.bmp"
  clean_background_svg = f"output/{base}/clean-background.svg"
  raw_vertices = f"output/{base}/raw-vertices.png"
  merged_vertices = f"output/{base}/merged-vertices.png"
  coordinates = f"output/{base}/vertex-coordinates.txt"
  walls = f"output/{base}/eroded-walls.png"
  walls_svg = f"output/{base}/eroded-walls.svg"

  # Return as object
  return IO(
    input,
    clean_background,
    clean_background_svg,
    raw_vertices,
    merged_vertices,
    coordinates,
    walls,
    walls_svg,
  )


def generate_output_folder(filename):
  base, _ = os.path.splitext(filename)  # Discard extension
  path = f"output/{base}"
  if not os.path.exists(path):
    os.makedirs(path)

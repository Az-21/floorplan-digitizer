import os
from dataclasses import dataclass


@dataclass(frozen=True)
class IO:
  input: str
  raw_vertices: str
  merged_vertices: str
  coordinates: str
  walls: str
  walls_svg: str


def io(filename):
  # Generate input path
  input = f"input/{filename}"

  # Generate outputs | Always save as .PNG
  base, _ = os.path.splitext(filename)  # Discard extension
  raw_vertices = f"output/{base}-raw-vertices.png"
  merged_vertices = f"output/{base}-merged-vertices.png"
  coordinates = f"output/{base}-vertex-coordinates.txt"
  walls = f"output/{base}-eroded-walls.png"
  walls_svg = f"output/{base}-eroded-walls.svg"

  # Return as object
  return IO(
    input,
    raw_vertices,
    merged_vertices,
    coordinates,
    walls,
    walls_svg,
  )

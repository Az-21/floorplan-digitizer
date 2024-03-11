import os


class IO:
  def __init__(self, input, raw_vertices, merged_vertices, coordinates, walls, walls_svg):
    self.input = input
    self.raw_vertices = raw_vertices
    self.merged_vertices = merged_vertices
    self.coordinates = coordinates
    self.walls = walls
    self.walls_svg = walls_svg


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

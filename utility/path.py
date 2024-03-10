import os


class IO:
  def __init__(self, input, raw_vertices, merged_vertices, coordinates):
    self.input = input
    self.raw_vertices = raw_vertices
    self.merged_vertices = merged_vertices
    self.coordinates = coordinates


def io(filename):
  # Generate input path
  input = f"input/{filename}"

  # Generate outputs | Always save as .PNG
  base, _ = os.path.splitext(filename)  # Discard extension
  raw_vertices = f"output/{base}-raw-vertices.png"
  merged_vertices = f"output/{base}-merged-vertices.png"
  coordinates = f"output/{base}-vertex-coordinates.txt"

  # Return as object
  return IO(input, raw_vertices, merged_vertices, coordinates)

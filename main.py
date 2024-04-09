from process import edge, merge, svg
from utility import path, save


def main():
  filename = "fp1.png"
  io = path.io(filename)

  # Vertex detection
  vertices = edge.detect(io.input, io.raw_vertices)
  merged_vertices = merge.close_vertices(io.input, io.merged_vertices, vertices, epsilon=12)
  save.vertices_as_txt(io.coordinates, merged_vertices)

  # Wall erosion -> SVG
  svg.detect_walls(io.input, io.walls)
  svg.generate_wall_svg(io.walls, io.walls_svg)


if __name__ == "__main__":
  main()

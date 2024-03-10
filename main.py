from process import edge
from process import merge
from utility import path
from utility import save


def main():
  filename = "fp1.png"
  io = path.io(filename)
  vertices = edge.detect(io.input, io.raw_vertices)
  merged_vertices = merge.close_vertices(io.input, io.merged_vertices, vertices, epsilon=12)
  save.vertices_as_txt(io.coordinates, merged_vertices)


if __name__ == "__main__":
  main()

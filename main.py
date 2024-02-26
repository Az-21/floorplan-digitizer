from process import edge
from process import merge
from utility import path

if __name__ == "__main__":
    filename = "fp1.png"
    io = path.io(filename)
    vertices = edge.detect(io.input, io.raw_vertices)
    merge.close_vertices(io.input, io.merged_vertices, vertices, epsilon=12)

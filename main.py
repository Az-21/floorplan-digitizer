import os
from process import edge
from process import merge

input = "input/fp1.png"
raw_vertex_output = "output/fp1-vertex.png"
merged_vertex_output = "output/fp1-merged.png"

if __name__ == "__main__":
    vertices = edge.detect(input, raw_vertex_output)
    merge.close_vertices(input, merged_vertex_output, vertices, epsilon=12)

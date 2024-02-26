import os
from process import edge

input = "input/fp1.png"
output = "output/fp1-vertex.png"

if __name__ == "__main__":
    vertices = edge.detect(input, output)

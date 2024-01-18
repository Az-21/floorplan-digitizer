import os
from process import edge_detection

if __name__ == "__main__":
    cwd = os.getcwd()
    edge_detection.detect_edges(cwd)

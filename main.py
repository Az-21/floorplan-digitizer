import blender.blender as blender
import clean.background
import config.config as cfg
import config.location as location
import postprocess.svg
from config.config import Config
from config.location import IO
from process import edge, merge
from utility import save


def main():
  # Read `config.json` and generate I/O paths
  config: Config = cfg.read_config()
  cfg.log_config(config)
  io: IO = location.generate_io_paths(config.filename)
  location.generate_output_folder(config.filename)

  # Vertex detection
  vertices = edge.detect(io, config)
  merged_vertices = merge.close_vertices(io, vertices, epsilon=12)
  save.vertices_as_txt(io.coordinates, merged_vertices)

  # Trace as SVG
  clean.background.run(io, config)
  postprocess.svg.trace(io, config)

  # Generate Blender action script
  blender.generate_bpy_script(io)


if __name__ == "__main__":
  main()

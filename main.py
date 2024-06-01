import src.blender.blender as blender
import src.clean.background
import src.clean.crop
import src.config.config as cfg
import src.config.location as location
import src.postprocess.svg
from src.config.config import Config
from src.config.location import IO
from src.process import edge, merge
from src.utility import save


def main() -> None:
  VERSION: str = "0.9.0"

  # Read `config.json` and generate I/O paths
  config: Config = cfg.read_config()
  cfg.log_config(config)
  io: IO = location.generate_io_paths(config.filename)
  location.generate_output_folder(config.filename)

  # Vertex detection
  vertices = edge.detect(io, config)
  merged_vertices = merge.close_vertices(io, vertices, epsilon=12)
  save.vertices_as_txt(io.coordinates, merged_vertices)

  # Cleanup
  src.clean.background.run(io, config)
  src.clean.crop.padding(io)

  # Trace as SVG and generate Blender action script
  src.postprocess.svg.trace(io, config)

  # Generate Blender action script
  blender.generate_bpy_script(io, config)


if __name__ == "__main__":
  main()

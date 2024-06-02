"""
This module serves as the main entry point for the application. It handles configuration reading,
vertex detection, image cleanup, SVG tracing, Blender script generation, and Typst document creation.

Modules:
- `blender`: Handles Blender script generation.
- `clean.background`: Handles background cleaning.
- `clean.crop`: Handles image cropping.
- `config.config`: Handles configuration reading and logging.
- `config.location`: Handles I/O path generation.
- `documentation.typst`: Handles Typst document generation.
- `postprocess.svg`: Handles SVG tracing.
- `process.edge`: Handles edge detection and vertex extraction.
- `process.merge`: Handles merging of close vertices.
- `utility.save`: Handles saving of vertices to a text file.

Functions:
- `main()`: Orchestrates the overall workflow of the application.
"""

import src.blender.blender as blender
import src.clean.background
import src.clean.crop
import src.config.config as cfg
import src.config.location as location
import src.documentation.typst as typst
import src.postprocess.svg
from src.config.config import Config
from src.config.location import IO
from src.process import edge, merge
from src.utility import save


def main() -> None:
  """
  Main function that orchestrates the workflow of the application.

  The function performs the following steps:
  1. Reads the configuration from `config.json`.
  2. Logs the configuration.
  3. Generates I/O paths based on the configuration filename.
  4. Creates the necessary output directories.
  5. Detects vertices in the input image.
  6. Merges close vertices.
  7. Saves the merged vertices to a text file.
  8. Runs background cleaning and image cropping.
  9. Traces the cleaned image to SVG format.
  10. Generates a Blender action script.
  11. Generates a Typst document.

  The version of the application is logged and used in the Typst document generation.
  """
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

  # Generate Typst document
  typst.generate_typst_document(io, config, VERSION)


if __name__ == "__main__":
  main()

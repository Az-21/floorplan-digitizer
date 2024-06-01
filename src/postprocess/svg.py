"""
This module provides functionality for tracing a cleaned background image and saving it as an SVG file.
It uses the Potrace executable to perform the tracing.

Dependencies:
- `subprocess`: Standard library for spawning new processes and connecting to their input/output/error pipes.
- `loguru.logger`: For logging information.
- `src.config.config.Config`: Custom class for configuration settings.
- `src.config.location.IO`: Custom class for input/output paths.

Functions:
- `trace(io: IO, config: Config) -> None`: Traces a cleaned background image and saves it as an SVG file.
"""

import subprocess
from loguru import logger
from src.config.config import Config
from src.config.location import IO


def trace(io: IO, config: Config) -> None:
  """
  Traces a cleaned background image and saves it as an SVG file using Potrace.

  Args:
      io (IO): An instance of the IO class containing input/output paths.
      config (Config): An instance of the Config class containing configuration settings.

  Process:
      1. Runs the Potrace executable with the given cropped image to generate an SVG file.
      2. Logs the completion of the tracing process.
  """
  subprocess.run([config.potrace_path, io.cropped, "-b", "svg"], capture_output=True)
  logger.info(f"Traced cleaned background image as SVG in `{io.svg}`")

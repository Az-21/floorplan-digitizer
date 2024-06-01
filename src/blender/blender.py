"""
This module provides functionality to generate a Blender Python script (.bpy) from a template.
It replaces placeholders in the template with specific values and saves the resulting script to a specified location.

Dependencies:
- `os`: Standard library for interacting with the operating system.
- `loguru.logger`: For logging information.
- `src.config.location.IO`: Custom class for input/output paths.
- `src.config.config.Config`: Custom class for configuration settings.
"""

import os
from loguru import logger
from src.config.location import IO
from src.config.config import Config


def generate_bpy_script(io: IO, config: Config) -> None:
  """
  Generates a Blender Python script by replacing placeholders in a template with actual values
  and saves the script to a specified location.

  Args:
      io (IO): An instance of the IO class containing input/output paths.
      config (Config): An instance of the Config class containing configuration settings.

  Process:
      1. Calls `_generate_full_svg_path(io)` to get the absolute path of the SVG file.
      2. Reads the Blender script template using `_read_blender_script_template()`.
      3. Replaces the placeholders `#SVG-PATH-PLACEHOLDER#`, `#SCALE-PLACEHOLDER#`, and
         `#HEIGHT-PLACEHOLDER#` in the template with actual values.
      4. Saves the modified template to the specified location using `_save_bpy_script(io, template)`.
      5. Logs an info message indicating the location where the script has been saved.
  """
  full_svg_path: str = _generate_full_svg_path(io)
  template: str = _read_blender_script_template()
  template = (
    template.replace("#SVG-PATH-PLACEHOLDER#", full_svg_path)
    .replace("#SCALE-PLACEHOLDER#", str(config.scale))
    .replace("#HEIGHT-PLACEHOLDER#", str(config.height))
  )
  _save_bpy_script(io, template)
  logger.info(f"Saved Blender action script in `{io.blender_script}`")


def _generate_full_svg_path(io: IO) -> str:
  """
  Generates the absolute path of the SVG file.

  Args:
      io (IO): An instance of the IO class containing input/output paths.

  Returns:
      str: The absolute path of the SVG file.
  """
  return os.path.abspath(io.svg)


def _read_blender_script_template() -> str:
  """
  Reads the Blender script template from a file.

  Returns:
      str: The content of the Blender script template.
  """
  with open("src/blender/blender_template.txt", "r") as file:
    return file.read()


def _save_bpy_script(io: IO, template: str) -> None:
  """
  Saves the modified Blender script template to a specified location.

  Args:
      io (IO): An instance of the IO class containing input/output paths.
      template (str): The modified Blender script template.
  """
  with open(io.blender_script, "w") as file:
    file.write(template)

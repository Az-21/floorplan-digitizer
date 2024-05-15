import os
from loguru import logger
from src.config.location import IO
from src.config.config import Config


def generate_bpy_script(io: IO, config: Config) -> None:
  full_svg_path: str = _generate_full_svg_path(io)
  template: str = _read_blender_script_template()
  template = (
    template.replace("#SVG-PATH-PLACEHOLDER#", full_svg_path)
    .replace("#SCALE-PLACEHOLDER#", str(config.scale))
    .replace("#HEIGHT-PLACEHOLDER#", str(config.height))
  )
  _save_bpy_script(io, template)
  logger.info(f"Saved Blender action script in `{io.blender_script}`\n")


def _generate_full_svg_path(io: IO) -> str:
  return os.path.abspath(io.svg)


def _read_blender_script_template() -> str:
  with open("src/blender/blender_template.txt", "r") as file:
    return file.read()


def _save_bpy_script(io: IO, template: str) -> None:
  with open(io.blender_script, "w") as file:
    file.write(template)

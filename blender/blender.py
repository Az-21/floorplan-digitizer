import os
from config.location import IO


def generate_bpy_script(io: IO) -> None:
  full_svg_path: str = _generate_full_svg_path(io)
  template = _read_blender_script_template()
  template: str = template.replace("#SVG-PATH-PLACEHOLDER#", full_svg_path)
  _save_bpy_script(io, template)


def _generate_full_svg_path(io: IO) -> str:
  return os.path.abspath(io.clean_background_svg)


def _read_blender_script_template() -> str:
  with open("blender/blender_template.txt", "r") as file:
    return file.read()


def _save_bpy_script(io: IO, template: str) -> None:
  with open(io.blender_script, "w") as file:
    file.write(template)

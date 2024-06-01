import os
import shutil
from datetime import datetime
import cv2
from loguru import logger
from src.config.config import Config
from src.config.location import IO


def generate_typst_document(io: IO, config: Config, version: str) -> None:
  template: str = _read_typst_script_template()

  time, date = _get_current_time()
  width, height = _get_image_dimensions(io.input)
  vertex_coordinates: str = _read_vertices(io)
  raw_svg: str = _read_raw_svg(io)
  raw_blender_script: str = _read_raw_blender_script(io)

  template = (
    template.replace("#VERSION-PLACEHOLDER#", version)
    .replace("#TIME-PLACEHOLDER#", time)
    .replace("#DATE-PLACEHOLDER#", date)
    .replace("#FILENAME-PLACEHOLDER#", str(config.filename))
    .replace("#THRESHOLD-PLACEHOLDER#", str(config.threshold_value))
    .replace("#TRI-PLACEHOLDER#", str(config.thickness_reduction_iterations))
    .replace("#TII-PLACEHOLDER#", str(config.thickness_increase_iterations))
    .replace("#SCALE-PLACEHOLDER#", str(config.scale))
    .replace("#HEIGHT-PLACEHOLDER#", str(config.height))
    .replace("#IMAGE-WIDTH-PLACEHOLDER#", str(width))
    .replace("#IMAGE-HEIGHT-PLACEHOLDER#", str(height))
    .replace("#VERTEX-LIST-PLACEHOLDER#", vertex_coordinates)
    .replace("#SVG-PLACEHOLDER#", raw_svg)
    .replace("#BLENDER-SCRIPT-PLACEHOLDER#", raw_blender_script)
  )

  shutil.copyfile(io.input, io.input_copy)  # Typst cannot read from parent directory, so a copy is made
  _save_typst_script(io, template)
  logger.info(f"Saved Typst document in `{io.typst_script}`\n")


def _read_typst_script_template() -> str:
  with open("src/documentation/typst_template.txt", "r") as file:
    return file.read()


def _get_current_time() -> tuple[str, str]:
  # return (time, date)
  return (datetime.now().strftime("%H:%M:%S"), datetime.now().strftime("%Y-%m-%d"))


def _get_image_dimensions(im_path: str) -> tuple[int, int]:
  im = cv2.imread(im_path)
  return im.shape[0], im.shape[1]


def _read_vertices(io: IO) -> str:
  with open(io.coordinates, "r") as file:
    return file.read()


def _read_raw_svg(io: IO) -> str:
  with open(io.svg, "r") as file:
    return file.read()


def _read_raw_blender_script(io: IO) -> str:
  with open(io.blender_script, "r") as file:
    return file.read()


def _generate_full_path(path: str) -> str:
  full_path: str = os.path.abspath(path)
  return full_path.replace("\\", "/")  # Typst prefers Unix path


def _save_typst_script(io: IO, template: str) -> None:
  with open(io.typst_script, "w") as file:
    file.write(template)

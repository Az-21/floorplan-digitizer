import subprocess
from loguru import logger
from src.config.config import Config
from src.config.location import IO


def trace(io: IO, config: Config) -> None:
  subprocess.run([config.potrace_path, io.clean_background, "-b", "svg"], capture_output=True)
  logger.info(f"Traced cleaned background image as SVG in `{io.clean_background_svg}`")

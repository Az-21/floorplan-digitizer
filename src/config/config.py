import json
import sys
from dataclasses import dataclass
from loguru import logger


@dataclass(frozen=True, slots=True)
class Config:
  filename: str
  threshold_value: int
  thickness_reduction_iterations: int
  thickness_increase_iterations: int
  potrace_path: str
  typst_path: str


# Function to read config.json and return as Config object
def read_config(path: str = "config.json") -> Config:
  with open(path) as file:
    data = json.load(file)
    return Config(
      data["filename"],
      data["threshold_value"],
      data["thickness_reduction_iterations"],
      data["thickness_increase_iterations"],
      data["potrace_path"],
      data["typst_path"],
    )


def log_config(config: Config) -> None:
  _check_exe_paths(config)
  logs: list[str] = []
  logs.append("Read configuration successfully")
  logs.append(f"Filename = {config.filename}")
  logs.append(f"Threshold value = {config.threshold_value}")
  logs.append(f"Thickness reduction iterations = {config.thickness_reduction_iterations}")
  logs.append(f"Thickness increase iterations = {config.thickness_increase_iterations}")
  logger.info("\n".join(logs))


# Ensure that the paths of the executables are set correctly
def _check_exe_paths(config: Config) -> None:
  error: bool = False
  if not config.potrace_path.endswith("potrace.exe"):
    error = True
    logger.error("Set the path of the `Potrace` executable in `config/config.json`")
    logger.info("Download from https://potrace.sourceforge.io/#downloading")

  if not config.typst_path.endswith("typst.exe"):
    error = True
    logger.error("Set the path of the `Typst` executable in `config/config.json`")
    logger.info("Download from https://github.com/typst/typst/releases/latest")

  if error:
    sys.exit()

"""
This module provides functionality for reading a configuration from a JSON file and logging the configuration details.
It also includes a class definition for the configuration settings using Python's `dataclass`.

Dependencies:
- `json`: Standard library for JSON operations.
- `sys`: Standard library for system-specific parameters and functions.
- `loguru.logger`: For logging information.

Classes:
- `Config`: A dataclass representing the configuration settings.

Functions:
- `read_config(path: str = "config.json") -> Config`: Reads configuration from a JSON file and returns a `Config` object.
- `log_config(config: Config) -> None`: Logs the configuration details and checks executable paths.
- `_check_exe_paths(config: Config) -> None`: Checks if the paths for Potrace and Typst executables are correctly set.
"""

import json
import sys
from dataclasses import dataclass
from loguru import logger


@dataclass(frozen=True, slots=True)
class Config:
  """
  A dataclass to hold configuration settings.

  Attributes:
      filename (str): The filename to be processed.
      threshold_value (int): The threshold value for image processing.
      thickness_reduction_iterations (int): The number of iterations to reduce thickness.
      thickness_increase_iterations (int): The number of iterations to increase thickness.
      potrace_path (str): The path to the Potrace executable.
      typst_path (str): The path to the Typst executable.
      scale (int): The scale factor for processing.
      height (float): The height parameter for processing.
  """

  filename: str
  threshold_value: int
  thickness_reduction_iterations: int
  thickness_increase_iterations: int
  potrace_path: str
  typst_path: str
  scale: int
  height: float


def read_config(path: str = "config.json") -> Config:
  """
  Reads configuration from a JSON file and returns a `Config` object.

  Args:
      path (str): The path to the JSON configuration file. Defaults to "config.json".

  Returns:
      Config: An instance of the `Config` dataclass containing the configuration settings.
  """
  with open(path) as file:
    data = json.load(file)
    return Config(
      data["filename"],
      data["threshold_value"],
      data["thickness_reduction_iterations"],
      data["thickness_increase_iterations"],
      data["potrace_path"],
      data["typst_path"],
      data["scale"],
      data["height"],
    )


def log_config(config: Config) -> None:
  """
  Logs the configuration details and checks executable paths.

  Args:
      config (Config): An instance of the `Config` dataclass containing the configuration settings.
  """
  _check_exe_paths(config)
  logs: list[str] = []
  logs.append("Read configuration successfully")
  logs.append(f"Filename = {config.filename}")
  logs.append(f"Threshold value = {config.threshold_value}")
  logs.append(f"Thickness reduction iterations = {config.thickness_reduction_iterations}")
  logs.append(f"Thickness increase iterations = {config.thickness_increase_iterations}")
  logger.info("\n".join(logs))


def _check_exe_paths(config: Config) -> None:
  """
  Checks if the paths for Potrace and Typst executables are correctly set.

  Args:
      config (Config): An instance of the `Config` dataclass containing the configuration settings.

  Logs an error and exits the program if the paths are not correctly set.
  """
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

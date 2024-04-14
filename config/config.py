import json
from dataclasses import dataclass


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

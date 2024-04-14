import subprocess
from config.config import Config
from config.location import IO


def trace(io: IO, config: Config) -> None:
  subprocess.run([config.potrace_path, io.clean_background, "-b", "svg"], capture_output=True)

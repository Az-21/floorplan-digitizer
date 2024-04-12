import subprocess
from config.location import IO


def trace(config: IO, potrace_path: str) -> None:
  subprocess.run([potrace_path, config.clean_background, "-b", "svg"], capture_output=True)

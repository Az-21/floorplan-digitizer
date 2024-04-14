import clean.background
import config.location as location
import postprocess.svg
import config.config as cfg


def main():
  # Read `config.json` and generate I/O paths
  config: cfg.Config = cfg.read_config()
  io = location.generate_io_paths(config.filename)
  location.generate_output_folder(config.filename)

  clean.background.run(io, threshold_value=100)
  postprocess.svg.trace(io, config.potrace_path)


if __name__ == "__main__":
  main()

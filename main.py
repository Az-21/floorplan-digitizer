import clean.background
import config.config as cfg
import config.location as location
import postprocess.svg


def main():
  # Read `config.json` and generate I/O paths
  config: cfg.Config = cfg.read_config()
  cfg.log_config(config)
  io = location.generate_io_paths(config.filename)
  location.generate_output_folder(config.filename)

  clean.background.run(io, config)
  postprocess.svg.trace(io, config)


if __name__ == "__main__":
  main()

import clean.background
import config.location as location
import postprocess.svg


def main():
  filename = "fp1.png"
  potrace_path = "potrace/exe/path/here"

  io = location.generate_io_paths(filename)
  location.generate_output_folder(filename)

  clean.background.run(io, threshold_value=100)
  postprocess.svg.trace(io, potrace_path)


if __name__ == "__main__":
  main()

import clean.background
import config.location as location


def main():
  filename = "fp1.png"
  io = location.generate_io_paths(filename)
  location.generate_output_folder(filename)

  clean.background.run(io, threshold_value=100)


if __name__ == "__main__":
  main()

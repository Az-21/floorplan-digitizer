import clean.background
import config.location as location


def main():
  filename = "fp1.png"
  io: location.IO = location.generate_io_paths(filename)

  clean.background.run(io)


if __name__ == "__main__":
  main()

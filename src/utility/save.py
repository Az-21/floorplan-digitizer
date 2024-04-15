from loguru import logger


def vertices_as_txt(filename, vertices) -> None:
  with open(filename, "w") as file:
    for vertex in vertices:
      x = round(vertex[0])
      y = round(vertex[1])
      coordinate = [x, y]
      file.write(str(coordinate) + "\n")
  logger.info(f"Saved simplified/merged vertex coordinates in `{filename}`")

from loguru import logger


def vertices_as_txt(filename: str, vertices: list[list[float]]) -> None:
  """
  Saves a list of vertex coordinates to a text file.

  Args:
      filename (str): The path to the file where the vertex coordinates will be saved.
      vertices (list[list[float]]): A list of vertex coordinates, where each vertex is represented by a list of two floats [x, y].

  Process:
      1. Opens the specified file for writing.
      2. Iterates over each vertex in the list.
      3. Rounds the x and y coordinates to the nearest integer.
      4. Writes the rounded coordinates to the file in the format [x, y].
      5. Logs a message indicating the file has been saved.
  """
  with open(filename, "w") as file:
    for vertex in vertices:
      x = round(vertex[0])
      y = round(vertex[1])
      coordinate = [x, y]
      file.write(str(coordinate) + "\n")
  logger.info(f"Saved simplified/merged vertex coordinates in `{filename}`")

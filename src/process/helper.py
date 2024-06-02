import os


def remove_extension(filename: str) -> str:
  """
  Removes the extension from a filename and returns the base name.

  Args:
      filename (str): The filename from which the extension will be removed.

  Returns:
      str: The base name of the file without the extension.

  Example:
      If the input filename is 'example.txt', the function will return 'example'.
  """
  base_name, _ = os.path.splitext(filename)
  return base_name

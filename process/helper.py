import os


def remove_extension(filename):
    base_name, extension = os.path.splitext(filename)
    return base_name

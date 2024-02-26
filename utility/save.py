def vertices_as_txt(filename, vertices):
    with open(filename, "w") as file:
        for vertex in vertices:
            file.write(str(vertex) + "\n")

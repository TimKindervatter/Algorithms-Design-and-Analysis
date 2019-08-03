import numpy as np
from pathlib import Path


def TSP_heuristic(vertex_labels, vertices, n):
    visited = {label: False for label in vertex_labels}
    visited[1] = True
    current_label = 1
    tour_length = 0
    count = 0

    while any(x is False for x in visited.values()):
        count += 1
        print(count)
        distances = []
        for label in vertex_labels:
            if not visited[label]:
                distances.append((label, np.linalg.norm(vertices[current_label-1] - vertices[label-1])))

        closest_vertex = min(distances, key=lambda x: (x[1], x[0]))  # Returns the closest vertex, with ties broken by smallest label
        visited[closest_vertex[0]] = True
        tour_length += closest_vertex[1]
        vertex_labels.remove(current_label)
        current_label = closest_vertex[0]
        
    tour_length += np.linalg.norm(vertices[current_label-1] - vertices[0])

    return tour_length


def read_input(filename):
    with open(filename) as f:
        n = int(f.readline())
        vertex_labels = []
        vertices = []
        for line in f.readlines():
            split_line = [float(x) for x in line.split()]
            vertex_labels.append(int(split_line[0]))
            vertices.append(split_line[1:])

    vertices = np.array(vertices)

    return vertex_labels, vertices, n


def read_output(filename):
    with open(filename) as f:
        expected = int(f.readline())

    return expected


if __name__ == "__main__":
    path = Path(__file__ + "../..").resolve()
    filename = Path(path, "nn.txt")
    
    vertex_labels, vertices, n = read_input(filename)

    tour_length = np.floor(TSP_heuristic(vertex_labels, vertices, n))
    expected = 1203406.0

    assert(tour_length == expected)
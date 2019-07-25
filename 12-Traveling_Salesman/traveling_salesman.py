import itertools
import numpy as np
from pathlib import Path


def traveling_salesman(vertices, n):
    subsets_containing_1 = generate_subsets(vertices, n)
    distances = get_distances(vertices, n)

    A = {}
    for S in subsets_containing_1:
        if len(S) == 1:
            A[(S, 1)] = 0
        else:
            A[(S, 1)] = np.inf

    for m in range(2, n+1):
        subsets_of_size_m = [x for x in subsets_containing_1 if len(x) == m]
        if m == n:
            paths_of_length_n = []
        for S in subsets_of_size_m:
            for j in S:
                if j == 1:
                    continue
                else:
                    path_lengths = []
                    
                    temp_list = [x for x in S if x is not j]
                    S_minus_j = tuple(temp_list)
                    for k in S:
                        if k == j:
                            continue
                        else:
                            path_lengths.append(A[(S_minus_j, k)] + distances[k-1, j-1])
                    A[(S, j)] = min(path_lengths)

                if m == n:
                    paths_of_length_n.append(A[S, j] + distances[j-1, 0])

    return min(paths_of_length_n)


def generate_subsets(vertices, n):
    vertex_labels = [x + 1 for x in range(n)]
    subsets = []
    for i in range(n + 1):
        for subset in itertools.combinations(vertex_labels, i):
            subsets.append(subset)

    subsets = [x for x in subsets if 1 in x]

    return subsets


def get_distances(vertices, n):
    distances = np.zeros([n, n])
    for j, vertex1 in enumerate(vertices):
        for k, vertex2 in enumerate(vertices):
            distances[j, k] = np.linalg.norm(vertex1 - vertex2)

    return distances


def read_input(filename):
    with open(filename) as f:
        n = int(f.readline())
        vertices = []
        for line in f.readlines():
            vertices.append([float(x) for x in line.split()])

    vertices = np.array(vertices)

    return vertices, n


def read_output(filename):
    with open(filename) as f:
        expected = int(f.readline())

    return expected


if __name__ == '__main__':
    path = Path(__file__ + "../..").resolve()
    vertices, n = read_input(Path(path, "tsp.txt"))

    set1 = [x for x in vertices if x[0] < 25000]
    set2 = [x for x in vertices if x[0] > 23700]

    tour1 = traveling_salesman(set1, len(set1))
    tour2 = traveling_salesman(set2, len(set2))

    common_edge_length = np.linalg.norm(vertices[12] - vertices[11])
    total_tour = tour1 + tour2 - 2*common_edge_length

    print(total_tour)
from pathlib import Path

def find_MST(graph):
    explored_nodes = []


if __name__ ==  '__main__':
    path = Path(__file__ + '../..').resolve()
    
    data = []
    with open(Path(path, "edges.txt")) as file:
        for line in file:
            data.append([int(x) for x in line.strip().split()])

    print(data)
import itertools
from pathlib import Path
from test_big_clustering import read_input
from UnionFind import UnionFind


def big_cluster(bitstrings, n, k=2):
    all_masks = generate_masks(n, k)
    values_present = {bitstring: True for bitstring in bitstrings}

    node_labels = [i for i in range(1, len(bitstrings) + 1)]
    nodes = {bitstring: i+1 for i, bitstring in enumerate(bitstrings)}

    clusters = UnionFind(node_labels)

    for bitstring in bitstrings:
        for mask in all_masks:
            masked_bitstring = bitstring_xor(bitstring, mask)
            if values_present.get(masked_bitstring):
                clusters.union(nodes[bitstring], nodes[masked_bitstring])

    return clusters


def bitstring_xor(a, b):
    y = int(a, 2) ^ int(b, 2)
    return bin(y)[2:].zfill(len(a))


def generate_masks(n, k):
    """ 
    Creates all permutations of a bit string with length n and <= k bits set.
    
    >>> generate_masks(3, 2)
    ['000', '100', '010', '001', '110', '101', '011']
    """

    all_masks = []
    for i in range(k+1):
        all_masks.extend(generate_hamming_masks(n, i))
        
    return all_masks


def generate_hamming_masks(n, k):
    """
    Generates all bit strings of length n which have k bits set
    
    >>> generate_hamming_masks(4, 3)
    ['1110', '1101', '1011', '0111']
    """

    masks = []
    for bits in itertools.combinations(range(n), k):
        bitstring = ['0'] * n
        for bit in bits:
            bitstring[bit] = '1'
        masks.append(''.join(bitstring))

    return masks


if __name__ == "__main__":
    path = Path(__file__ + "../..").resolve()
    bitstrings = []
    with open(Path(path, 'clustering_big.txt')) as file:
        first_line = file.readline().split()
        num_nodes = int(first_line[0])
        n = int(first_line[1])
        for line in file.readlines():
            line = line.strip().replace(" ", "")
            bitstrings.append(line)

    clusters = big_cluster(bitstrings, n)

    print(len(clusters))
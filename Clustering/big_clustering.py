import itertools
from UnionFind import UnionFind


def big_cluster(bitstrings, n, k):
    all_masks = generate_masks(n, k)
    values_present = {bitstring: True for bitstring in bitstrings}

    for bitstring in bitstrings:
        clusters = UnionFind(bitstrings)

        for mask in all_masks:
            masked_bitstring = bitstring_xor(bitstring, mask)
            if values_present[masked_bitstring]:
                clusters.union(bitstring, masked_bitstring)

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
    bitstrings = ["000", "001", "010", "011", "100", "101", "110", "111"]
    n = 3
    k = 2

    clusters = big_cluster(bitstrings, n, k)

    print(clusters)
    print(len(clusters))
import heapq
from pathlib import Path
from BinaryTree import BinaryTree


def huffman(symbol_weights):
    symbols = [(symbol_weight, BinaryTree(root=symbol_weight)) for symbol_weight in symbol_weights]
    for _ in range(len(symbols) - 1):
        heapq.heapify(symbols)

        lightest_symbol = heapq.heappop(symbols)
        second_lightest_symbol = heapq.heappop(symbols)

        merged_symbol = merge_symbols(lightest_symbol, second_lightest_symbol)

        heapq.heappush(symbols, merged_symbol)

    symbol_tree = symbols[0][1]
    return symbol_tree


def merge_symbols(lightest_symbol, second_lightest_symbol):
    merged_weight = lightest_symbol[0] + second_lightest_symbol[0]
    merged_node = BinaryTree(lightest_symbol[1], second_lightest_symbol[1], merged_weight)

    return (merged_weight, merged_node)


def read_input(filename):
    symbol_weights = []
    with open(filename) as f:
        number_of_symbols = int(f.readline())
        for line in f.readlines():
            symbol_weights.append(int(line))

    return symbol_weights


def read_output(filename):
    depths = []
    with open(filename) as f:
        for line in f.readlines():
            depths.append(int(line))
    
    return depths


if __name__ == '__main__':
    path = Path(__file__ + '../..').resolve()
    filename = Path(path, 'huffman.txt')
    symbol_weights = read_input(filename)

    symbol_tree = huffman(symbol_weights)

    max_depth = symbol_tree.max_depth
    min_depth = symbol_tree.min_depth

    print([max_depth, min_depth])
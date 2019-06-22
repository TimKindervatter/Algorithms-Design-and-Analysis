import heapq
from BinaryTree import BinaryTree


# class Huffman_Node:
#     def __init__(self, left=None, right=None):
#         self.left = left
#         self.right = right

#     def __lt__(self, other):
#         return False


def huffman(symbol_weights):
    symbols = [(symbol_weight, BinaryTree(root=symbol_weight)) for symbol_weight in symbol_weights]
    for _ in range(len(symbols) - 1):
        heapq.heapify(symbols)

        lightest_symbol = heapq.heappop(symbols)
        second_lightest_symbol = heapq.heappop(symbols)

        merged_symbol = merge_symbols(lightest_symbol, second_lightest_symbol)

        heapq.heappush(symbols, merged_symbol)

    return symbols


def merge_symbols(lightest_symbol, second_lightest_symbol):
    merged_weight = lightest_symbol[0] + second_lightest_symbol[0]
    merged_node = BinaryTree(lightest_symbol[1], second_lightest_symbol[1], merged_weight)

    return (merged_weight, merged_node)


if __name__ == '__main__':
    # symbol_weights = [3, 2, 6, 8, 2, 6]
    # symbol_weights = [60, 25, 10, 5]
    symbol_weights = [74, 46, 25, 48, 13, 37, 97, 77, 45, 96]
    print(huffman(symbol_weights))
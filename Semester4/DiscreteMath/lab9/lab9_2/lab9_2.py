import heapq
import os
from collections import Counter


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    freq = Counter(text)
    priority_queue = [HuffmanNode(char, f) for char, f in freq.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]


def build_huffman_codes(root):
    codes = {}
    
    def build_code(node, code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = code
            return
        build_code(node.left, code + '0')
        build_code(node.right, code + '1')
    build_code(root, '')
    return codes


def compress_file(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()

    root = build_huffman_tree(text)
    codes = build_huffman_codes(root)

    compressed_text = ''.join(codes[char] for char in text)
    padding_length = 8 - len(compressed_text) % 8
    compressed_text += padding_length * '0'

    bytes_ = [compressed_text[i:i + 8] for i in range(0, len(compressed_text), 8)]
    bytes_ = [int(byte, 2) for byte in bytes_]

    bytes_as_bytes = bytes(bytes_)
    
    with open(output_file, 'wb') as f:
        f.write(bytes_as_bytes)

    return codes


def main():
    input_file = input("Enter the path to the input file: ")
    output_file = 'lab9_2/files/compressed_text_short.bin'

    if not os.path.exists(input_file):
        print("Input file not found.")
        return

    codes = compress_file(input_file, output_file)
    print("Compression successful.")
    print("Huffman Codes:")
    for char, code in codes.items():
        print(f"{char}: {code}")


if __name__ == "__main__":
    main()

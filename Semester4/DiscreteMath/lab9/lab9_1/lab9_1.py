import os

from collections import Counter

import math


def shannon_entropy(data):
    entropy = 0.0
    length = len(data)
    freqs = Counter(data)
    for freq in freqs.values():
        prob = freq / length
        entropy -= prob * math.log2(prob)
    return entropy


def calculate_compression_ratio(original_file, compressed_file):
    original_size = os.path.getsize(original_file)
    compressed_size = os.path.getsize(compressed_file)
    compression_ratio = original_size / compressed_size
    return compression_ratio


def main():
    original_file = input("Enter the path to the original file: ")
    compressed_file = input("Enter the path to the compressed file: ")

    if not os.path.exists(original_file) or not os.path.exists(compressed_file):
        print("File not found.")
        return

    with open(original_file, 'rb') as f:
        data = f.read()
        entropy = shannon_entropy(data)
        print(f"Entropy of the original file: {entropy:.2f}")

    compression_ratio = calculate_compression_ratio(original_file, compressed_file)
    print(f"Compression ratio: {compression_ratio:.2f}")


if __name__ == "__main__":
    main()

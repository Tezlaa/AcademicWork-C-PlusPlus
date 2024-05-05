class LZ77:
    def __init__(self, window_size, lookahead_buffer_size):
        self.window_size = window_size
        self.lookahead_buffer_size = lookahead_buffer_size

    def compress(self, data):
        compressed_data = []
        index = 0
        while index < len(data):
            match_length = 0
            match_offset = 0
            for i in range(1, min(self.lookahead_buffer_size, len(data) - index) + 1):
                substring = data[index:index + i]
                if substring in data[max(0, index - self.window_size):index]:
                    match_length = i
                    match_offset = index - data.rindex(substring, max(0, index - self.window_size), index)
            if match_length > 0:
                compressed_data.append((match_offset, match_length, data[index + match_length]))
                index += match_length + 1
            else:
                compressed_data.append((0, 0, data[index]))
                index += 1
        return compressed_data

    def decompress(self, compressed_data):
        decompressed_data = ""
        for item in compressed_data:
            if item[0] == 0:
                decompressed_data += item[2]
            else:
                start = len(decompressed_data) - item[0]
                end = start + item[1]
                decompressed_data += decompressed_data[start:end] + item[2]
        return decompressed_data

# Example usage:
window_size = 12
lookahead_buffer_size = 5
lz77 = LZ77(window_size, lookahead_buffer_size)

with open("lab9_3/files/input.txt", "r") as f:
    data = f.read()

print("Original data:", data)
compressed_data = lz77.compress(data)
print("Compressed data:", compressed_data)

decompressed_data = lz77.decompress(compressed_data)
print("Decompressed data:", decompressed_data)

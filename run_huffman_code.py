from Huffman_Coding import HuffmanCoding
import sys

path = "sample.txt"

h = HuffmanCoding(path)

compressed_path = h.compress()
print("Compressed File Name: " + compressed_path)


decompressed_path = h.decompress(compressed_path)
print("Decompressed File Name: " + decompressed_path)
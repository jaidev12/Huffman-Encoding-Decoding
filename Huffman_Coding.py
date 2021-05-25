import heapq
import os

class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None
        
        def __lt__(self, other):
            return self.freq < other.freq
        
        def __eq__(self, other):
            if(other == None):
                return False
            if(not isinstance(other, HeapNode)):
                return False
            return self.freq == other.freq
    
class HuffmanCoding:
    def __init__(self, path):
        self.heap = []
        self.path = path
        self.codes = {}
        self.reverse_mapping = {}

   
    def make_freq_dict(self, text):
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency

    def make_heap(self, frequency):
        for key in frequency:
            node = HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)
    
    def merge_nodes(self):
        while(len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            
            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)
    
    def make_codes_helper(self, node, current_code):
        if(node == None):
            return
        if(node.char != None):
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char
            return

        self.make_codes_helper(node.left, current_code + "0")
        self.make_codes_helper(node.right, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_encoded_text(self, text): 
        encoded_text = ""
        #print(self.codes)
        for character in text:
                    encoded_text += self.codes[character]
        return encoded_text

    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - (len(encoded_text) % 8)
        for i in range(extra_padding):
            encoded_text += "0"
        
        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

    def get_byte_array(self, padded_encoded_text):
        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i : i + 8]
            b.append(int(byte, 2))
        
        return b

    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"
        
        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency = self.make_freq_dict(text)
            self.make_heap(frequency)
            self.merge_nodes()
            self.make_codes()

            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)

            x = self.get_byte_array(padded_encoded_text)

            output.write(bytes(x))

            print("FILE COMPRESSED")
            return output_path

    def remove_padding(self, bit_string):
        padded_info = bit_string[:8]
        extra_padding = int(padded_info, 2)
        bit_string = bit_string[8:]

        encoded_text = bit_string[:-1*extra_padding]

        return encoded_text

    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""
        
        return decoded_text
    
    def decompress(self, input_path):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed.txt"

        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ""
            byte = file.read(1)
            while(len(byte) > 0):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)
            
            encoded_text = self.remove_padding(bit_string)
            decompressed_text = self.decode_text(encoded_text)
        
            output.write(decompressed_text)

        print("FILE DECOMPRESSED")

        return output_path




   

        
    
# Huffman-Encoding-Decoding

Huffman coding is a lossless data compression algorithm. The idea is to assign variable-length codes to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters. The most frequent character gets the smallest code and the least frequent character gets the largest code.
The variable-length codes assigned to input characters are Prefix Codes, means the codes (bit sequences) are assigned in such a way that the code assigned to one character is not the prefix of code assigned to any other character. This is how Huffman Coding makes sure that there is no ambiguity when decoding the generated bitstream. 
Let us understand prefix codes with a counter example. Let there be four characters a, b, c and d, and their corresponding variable length codes be 00, 01, 0 and 1. This coding leads to ambiguity because code assigned to c is the prefix of codes assigned to a and b. If the compressed bit stream is 0001, the de-compressed output may be “cccd” or “ccb” or “acd” or “ab”.
See this for applications of Huffman Coding. 
There are mainly two major parts in Huffman Coding
1. Build a Huffman Tree from input characters.
2. Traverse the Huffman Tree and assign codes to characters.

Building Huffman Tree:
1. Extract 2 minimum nodes from the queue.
2. Merge(sum) these nodes to create a new node.
3. Make this new node as the parent of the 2 extracted nodes.
4. Insert the new node into the Priority Queue.
5. Repeat the above steps until only 1 node is left in the priority queue.

Assign Codes using Huffman Tree:
1. Assign 0 to left edges and 1 to right edges
2. Traverse tree from root to characters and build codes for each

Compression(Huffman Encoding):
Replace character in your data with there codes. 
Overall size of new file will be less than that of the original file.

Decompression(Huffman Decoding):
Start Reading bits of your encoded file.
Whenever you find that a particular bit sequence is a valid code, replace it with its character.

Steps for Compression:
1. Build frequency dictionary(count of occurences of all characters)
2. Build Priority Queue(Used Minheap)
3. Build Huffman Tree by selecting 2  minimum nodes(whose occurences are least) and merging them.
4. Assign codes to characters(Also store Huffman codes mapping while compression)
5. Encode Input Text(replace character with its code)
6. If overall length of bit stream is not multiple of 8, add some padding to text.
7. Store this padding information(8bits) at start of overall encoded bit stream.
8. Write result to an Output Binary File.

Steps for Decompression:
1. Read Binaryt File.
2. Read padding information and remove the padded bits.
3. Decode the bits - read bits & replace the valid huffman code bits with character values.
4. Save decoded data into Output File.





# Function to compute the frequencies of characters in a string
def compute_character_frequencies(string):
    frequencies = {}
    for char in string:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies

# Huffman Encoder using a BinaryTree implementation
class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

# repeatedly merging two nodes with the lowest frequencies
def build_huffman_tree(frequencies):
    nodes = []
    for char, freq in frequencies.items():
        nodes.append(Node(char=char, freq=freq))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = Node(char=None, freq=left.freq + right.freq)
        parent.left = left
        parent.right = right
        nodes.append(parent)

    return nodes[0]

# Function recursively traverses the Huffman tree and assigns the binary codes to each character
def build_huffman_codes(node, current_code, codes):
    if node.char:
        codes[node.char] = current_code
        return

    build_huffman_codes(node.left, current_code + "0", codes)
    build_huffman_codes(node.right, current_code + "1", codes)

def huffman_encode(string):
    frequencies = compute_character_frequencies(string)
    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = {}
    build_huffman_codes(huffman_tree, "", huffman_codes)

    encoded_string = ""
    for char in string:
        encoded_string += huffman_codes[char]

    return encoded_string, huffman_codes

# Example usage of the huffman encoding a text
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
encoded_string, huffman_codes = huffman_encode(text)
print("Encoded string:", encoded_string)
print("Huffman codes:", huffman_codes)

# Huffman Decoder function
def huffman_decode(encoded_string, huffman_codes):
    reversed_codes = {v: k for k, v in huffman_codes.items()}
    decoded_string = ""
    current_code = ""
    for bit in encoded_string:
        current_code += bit
        if current_code in reversed_codes:
            decoded_string += reversed_codes[current_code]
            current_code = ""
    return decoded_string

# Example usage of the decoder
decoded_string = huffman_decode(encoded_string, huffman_codes)
print("Decoded string:", decoded_string)
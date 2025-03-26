

def create_huffman_tree(frequency_table: list):
    if len(frequency_table) == 1:
        return frequency_table[0]
    while len(frequency_table) > 1:
        item1 = frequency_table.pop()
        item2 = frequency_table.pop()
        print(f"Combining frequency of {item1.character} and {item2.character}.")
        new_frequency = item1.frequency + item2.frequency
        print(f"New frequency is {new_frequency}.")
        new_node = Node(new_frequency)
        new_node.left = item1
        new_node.right = item2
        frequency_table.append(new_node)
        frequency_table = sorted(frequency_table, key=lambda nod: nod.frequency, reverse=True)
    print(frequency_table)
    return frequency_table[0]


def create_binary_codes(node, code, huffman_codes):
    ''' Recursive method that traverses down every node to the left, then every node to the right for each node. '''
    # very specific edge case that occurs when the input is all one of the smae character e.g. "a", or "555555"
    if code == '' and node.left is None and node.right is None and node.character is not None:
        huffman_codes[node.character] = '0'
        return huffman_codes
    if node is None:
        return huffman_codes
    if node.character is not None:
        huffman_codes[node.character] = code
    create_binary_codes(node.left, code + '0', huffman_codes)
    create_binary_codes(node.right, code + '1', huffman_codes)
    return huffman_codes


def create_compressed_string(huffman_codes, input_string):
    asc_val = 0
    compressed_string = ''
    for character in input_string:
        asc_val += ord(character)
        compressed_string += huffman_codes[character]
    return (asc_val, compressed_string)


def decode_compressed_string(huffman_tree, compressed_string):
    checksum = compressed_string[0]
    code = compressed_string[1]
    output = ''
    current_node = huffman_tree
    for binary in code:
        if binary == '0':
            # covers a specific edge case when input string is all same character i.e "aaaaaaaaaaaaaa"
            if current_node.left is not None:
                current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.character is not None:
            output += current_node.character
            current_node = huffman_tree
    decompressed_checksum = 0
    for character in output:
        decompressed_checksum += ord(character)
    if checksum != decompressed_checksum:
        raise Exception("Data may be corrupted")
    return (decompressed_checksum, output)


class Node:
    def __init__(self, frequency, character=None):
        self.frequency = frequency
        self.character = character
        self.left = None
        self.right = None
    def __repr__(self):
        return f'({self.frequency}, {self.character})'
    

def test_huffman_compression(input_string):    
    FT = [
        Node(20,'A'),
        Node(15,'B'),
        Node(12,'C'),
        Node(10,'D'),
        Node(9,'E'),
        Node(7,'F'),
        Node(6,'G'),
        Node(5,'H'),
        Node(4,'I'),
        Node(3,'J'),
        Node(2,'K'),
        Node(2,'L'),
        Node(2,'M'),
        Node(1,'N'),
        Node(1,'S'),
    ]
    ft_copy = FT.copy()

    ht = create_huffman_tree(FT)
    print()
    bc = create_binary_codes(ht, '', {})
    print('Binary Codes:')
    for c in bc.items():
        print(c)
    print()
    cs = create_compressed_string(bc, input_string)
    print(f"Encoded string: {cs[1]}")
    print(f"Ascii Total: {cs[0]}")
    print()
    ds = decode_compressed_string(ht, cs)
    print(f"Decoded string: {ds[1]}")
    print()
    return {"ft": ft_copy, "ht": ht, "bc": bc, "cs": cs, "input": input_string}


if __name__ == '__main__':
    x = test_huffman_compression('JINGLEBELLS')
    compressed_size = len(x['cs'][1])
    fixed_encode_size = len('JINGLEBELLS') * 4
    print(f"Compressed Size: {compressed_size}")
    print(f"Fixed Encoding Size: {fixed_encode_size}")

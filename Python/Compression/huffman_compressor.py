

def create_frequency_table(input_string: str):
    f_table_dict = {}
    for character in input_string:
        if character in f_table_dict.keys():
            f_table_dict[character] += 1
        else:
            f_table_dict[character] = 1
    f_table_list = [Node(v, k) for k, v in f_table_dict.items()]
    f_table_list = sorted(f_table_list, key=lambda nod: nod.frequency, reverse=True)
    return f_table_list


def create_huffman_tree(frequency_table: list):
    if len(frequency_table) == 1:
        return frequency_table[0]
    while len(frequency_table) > 1:
        item1 = frequency_table.pop()
        item2 = frequency_table.pop()
        new_frequency = item1.frequency + item2.frequency
        new_node = Node(new_frequency)
        new_node.left = item1
        new_node.right = item2
        frequency_table.append(new_node)
        frequency_table = sorted(frequency_table, key=lambda nod: nod.frequency, reverse=True)
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


class Node:
    def __init__(self, frequency, character=None):
        self.frequency = frequency
        self.character = character
        self.left = None
        self.right = None
    def __repr__(self):
        return f'({self.frequency}, {self.character})'
    

def test_huffman_compression(input_string):
    
    ft = create_frequency_table(input_string)
    ht = create_huffman_tree(ft)
    bc = create_binary_codes(ht, '', {})
    cs = create_compressed_string(bc, input_string)
    return {"ft": ft, "ht": ht, "bc": bc, "cs": cs, "input": input_string}

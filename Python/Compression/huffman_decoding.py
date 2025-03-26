

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


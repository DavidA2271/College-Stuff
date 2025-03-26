import huffman_compressor as compress
import huffman_decoding as decode


def main():
    test_compression('a')
    test_compression('a1')
    test_compression('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    test_compression('asidfbviaubrvi')
    test_compression('hello hi')
    test_compression('1274t6^&%$$*&%$jbfgsbf\'\'\'\'sbwigcdf ')
    test_compression('0123456789QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm[]\;\',./\{\}|:\"<>?-=_+!@#$%^&*()`~')


def test_compression(input_string):
    compressed = compress.test_huffman_compression(input_string)
    print('Input:', input_string, "\tCompressed Code:", compressed['cs'][1], "\tChecksum:", compressed['cs'][0])
    decoded = decode.decode_compressed_string(compressed['ht'], compressed['cs'])
    print('Decoded String:', decoded[1], "\tDecoded Checksum:", decoded[0])

    original_binary = ''.join(format(ord(x), 'b') for x in input_string)
    print("Uncompressed Binary: ", original_binary)
    original_size = len(original_binary)
    compressed_size = len(compressed['cs'][1])
    print("Original Binary Size:", original_size, "\tCompressed Binary Size:", compressed_size)
    print("Reduction:", f"{int((1 - float(compressed_size/original_size)) * 100)}% reduction")
    print()
    print()


if __name__ == '__main__':
    main()

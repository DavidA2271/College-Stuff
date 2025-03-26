
class Hexdumper:
    ''' Reads binary files and can output them in various formats. '''
    def __init__(self) -> None:
        self._filename = ''
        self._buffer_size = 4
    def target_file(self, filename: str, buffer_size: int=4):
        ''' Tells hexadump what file to target and how much you want to read at a time.
         
            buffer_size: int kilobytes read at a time
        '''
        self._filename = filename
        self._buffer_size = buffer_size
    def show_ascii(self, reverse=False):
        ''' Prints the ascii values of your file '''
        with open(self._filename, 'rb') as fin:
            for chunk in self._read_in_chunks(fin, 2**10*self._buffer_size): # 4KB default
                asc = self.process_chunks(chunk, _Mode.ASCII, reverse)
                print(''.join(asc))
    def show_decimal(self, reverse=False):
        ''' Prints the decimal values of your file '''
        with open(self._filename, 'rb') as fin:
            for chunk in self._read_in_chunks(fin, 2**10*self._buffer_size): # 4KB default
                dec = self.process_chunks(chunk, _Mode.DECIMAL, reverse)
                print(' '.join(dec))
    def show_hex(self):
        ''' Prints the hexadecimal values of your file '''
        with open(self._filename, 'rb') as fin:
            for chunk in self._read_in_chunks(fin, 2**10*self._buffer_size): # 4KB default
                hx = self.process_chunks(chunk, _Mode.HEX)
                print(' '.join(hx))
    def show_oct(self):
        ''' Prints the octal values of your file '''
        with open(self._filename, 'rb') as fin:
            for chunk in self._read_in_chunks(fin, 2**10*self._buffer_size): # 4KB default
                oc = self.process_chunks(chunk, _Mode.OCTAL)
                print(' '.join(oc))
    def _read_in_chunks(self, fin, buffer_size):
        ''' Reads the file in chunks '''
        while True:
            data = fin.read(buffer_size)
            if not data:
                break
            yield data
    def process_chunks(self, chunk: bytes, mode: str, reverse=False):
        ''' Converts bytes into the format specified by the mode parameter '''
        bit_list = []
        for i in range(0, len(chunk), 2):
            bitpair = []
            if mode == _Mode.DECIMAL:
                bitpair.append(str(chunk[i]))
                bitpair.append(str(chunk[i+1]))
            elif mode == _Mode.ASCII:
                bitpair.append(chr(chunk[i]))
                bitpair.append(chr(chunk[i+1]))
            elif mode == _Mode.HEX:
                bit_list.append(hex(chunk[i]))
                bit_list.append(hex(chunk[i+1]))
                continue
            elif mode == _Mode.OCTAL:
                bit_list.append(oct(chunk[i]))
                bit_list.append(oct(chunk[i+1]))
                continue
            if reverse:
                bitpair.reverse()
            pair = ''.join(bitpair)
            bit_list.append(pair)
        return bit_list
    

class _Mode:
    ''' Class for hexdumper modes. '''
    ASCII = 'ascii'
    DECIMAL = 'decimal'
    HEX = 'hex'
    OCTAL = 'octal'

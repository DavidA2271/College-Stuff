

class FileReader:
    ''' Class to read lines from a text file '''
    def __init__(self, filename) -> None:
        self.lines = []
        self._get_lines_from_file(filename)
    def _get_lines_from_file(self, filename):
        with open(filename, 'r') as handle:
            for line in handle:
                line = line.strip()
                self.lines.append(line)


class MyIterator:
    ''' Class that acts as an iterator. It can get the next line, previous line, or a specific line. '''
    def __init__(self, file_reader: FileReader) -> None:
        self.position = -1
        self.lines = file_reader.lines
    def next(self):
        ''' Gets the next line '''
        try:
            return self.get(self.position + 1)
        except IndexError:
            print('No more next lines')
    def prev(self):
        ''' Gets the previous line '''
        try:
            return self.get(self.position - 1)
        except IndexError:
            print('No more previous lines')
    def get(self, index):
        ''' Gets the line at the specified index '''
        line = self.lines[index]
        self.position = index
        return line
    

class Program:
    ''' Class that runs the program '''
    def __init__(self) -> None:
        self.ih = InputHandler()
        self._setup()
        self.run()
    def _setup(self):
        filename = self.ih._ask_for_file()
        fr = FileReader(filename)
        self.iterator = MyIterator(fr)
        self.ih._display_help_message()
    def run(self):
        ''' Always runs while the program is running '''
        while True:
            command = self.ih._wait_for_command()
            self._process_command(command)
    def _process_command(self, cmd:str):
        ''' Processes commands inputted by user '''
        print()
        if cmd == '': # for when the user wants some space before putting in a command
            pass
        elif cmd == 'help':
            self.ih._display_commands()
        elif cmd == 'first':
            line = self.iterator.get(0)
            print('This is the first line:')
            print(line)
        elif cmd == 'last':
            while self.iterator.next() is not None:
                line = self.iterator.next()            
            print('This is the last line:')
            print(line)
        elif cmd == 'next':
            line = self.iterator.next()
            if line is not None:
                print('This is the next line:')
                print(line)
        elif cmd == 'prev':
            line = self.iterator.prev()
            if line is not None:
                print('This is the previous line:')
                print(line)
        elif cmd.__contains__('get '):
            cmd = cmd.strip()
            try:
                index = int(cmd.split(sep=' ')[1])
                line = self.iterator.get(index)
                print(f'This is line {index}:')
                print(line)
            except ValueError:
                print('Line to get was not of type int')
            except IndexError:
                print('Index was out of bounds')            
        else:
            print(f'{cmd} is not a valid command')
            print()
            self.ih._display_commands()
        print()



class InputHandler:
    ''' Handles user input and prints general messages. '''
    def _ask_for_file(self):
        return input('Enter the name of your file:\t')
    def _display_help_message(self):
        print('Type \"help\" at any time to get a list of commands.\n')
    def _display_commands(self):
        print('--------------------------------------------------')
        print('                    Commands')
        print('--------------------------------------------------')
        print('    help - print a list of commands')
        print('    first - get the first line')
        print('    last - get the last line')
        print('    next - get the next line')
        print('    prev - get the previous line')
        print('    get [index] - get the line at the given index')
        print('--------------------------------------------------')
    def _wait_for_command(self):
        return input()
    

if __name__ == '__main__':
    Program()

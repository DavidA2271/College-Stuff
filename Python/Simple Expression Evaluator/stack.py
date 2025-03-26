

class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        return value

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def print_stack(self) -> None:
        for i in self.stack:
            print(i, end=" ")
        print()

    def empty(self) -> bool:
        return not len(self.stack) > 0
    
    def clear(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)
        

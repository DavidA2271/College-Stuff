

class Queue:
    def __init__(self) -> None:
        self.queue = []

    def push(self, value):
        self.queue.append(value)
        return value

    def peek(self):
        if not self.queue:
            return None
        return self.queue[0]

    def pop(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    def print_queue(self) -> None:
        for i in self.queue:
            print(i, end=" ")
        print()

    def empty(self) -> bool:
        return not len(self.queue) > 0
    
    def clear(self):
        self.queue = []
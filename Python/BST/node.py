

class Node:
    def __init__(self) -> None:
        self.value = None
        self.left = None
        self.right = None
        self.parent = None
        self.color = "red"
    def grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent
    def sibling(self):
        if self.parent is None:
            return None
        if self == self.parent.left:
            return self.parent.right
        return self.parent.left
    def uncle(self):
        if self.parent is None:
            return None
        return self.parent.sibling()
    def __str__(self) -> str:
        return f'Value: {self.value}'


class Operator:
    def __init__(self, operator: str, precedence: int, association: str) -> None:
        self.operator = operator
        self.precedence = precedence
        self.association = association

    def __repr__(self) -> str:
        return "(" + self.operator + ", " + str(self.precedence) + ", " + self.association + ")"
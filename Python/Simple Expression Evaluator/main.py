import sys
import my_exceptions
from que import Queue
from stack import Stack
from operater import Operator


operators: dict[str, Operator] = {
    "+" : Operator("+", 1, "left"),
    "-" : Operator("-", 1, "left"),
    "*" : Operator("*", 2, "left"),
    "/" : Operator("/", 2, "left"),
    "^" : Operator("^", 3, "right")
}


def shunting_yard(exp: str):
    output: Queue = Queue()
    operator: Stack = Stack()    
    for c in exp:
        if c == " ":
            continue
        elif c.isalpha():
            raise my_exceptions.InvalidCharacterException
        elif c.isdecimal():
            output.push(c)        
        elif c == "(":
            operator.push(c)
        elif c ==")":
            if operator.empty():
                raise my_exceptions.MissingParenthesisException
            while operator.peek() != "(":
                output.push(operator.pop().operator)
                if operator.empty():
                    raise my_exceptions.MissingParenthesisException
            operator.pop()
        elif c in operators.keys():
            op = operators[c]
            while (not operator.empty() and
                   operator.peek() != "(" and
                   (operator.peek().precedence > op.precedence or
                    (op.association == "left" and operator.peek().precedence == op.precedence))):
                output.push(operator.pop().operator)
            operator.push(op)
    if not operator.empty():
        while not operator.empty():
            if operator.peek() == "(":
                raise my_exceptions.MissingParenthesisException
            else:
                output.push(operator.pop().operator)
    return output


def evaluate_postfix(postfix: Queue):
    call_stack: Stack = Stack()
    while not postfix.empty():
        c = postfix.pop()
        if c.isdecimal():
            call_stack.push(c)
        elif c in operators.keys():
            if len(call_stack) < 2:
                raise my_exceptions.TooManyOperatorsException        
            right_val = call_stack.pop()
            left_val = call_stack.pop()
            if c == "/" and right_val == "0":
                raise my_exceptions.DivideByZeroException
            if c == "^":
                c = "**"
            res = eval(left_val + c + right_val)
            call_stack.push(str(res))
    if len(call_stack) == 1:
        return call_stack.pop()
    else:
        raise Exception()


def main(args):
    print("Input:")
    print(args)
    print()

    if args[0] == "\"":
        args = args[1:-2]

    try:
        postfix = shunting_yard(args)
    except my_exceptions.InvalidCharacterException:
        print("Invalid Characters Detected")
        return
    except my_exceptions.MissingParenthesisException:
        print("Missing a Parenthesis")
        return
    print("Postfix Notation:")
    postfix.print_queue()
    print()
    
    try:
        result = evaluate_postfix(postfix)    
    except my_exceptions.TooManyOperatorsException:
        print("Too Many Operators")
        return
    except my_exceptions.DivideByZeroException:
        print("Cannot Divide By Zero")
        return
    except Exception:
        return
    print("Result:")
    print(str(result))
    print()
    print()
        

if __name__ == "__main__":
    main(sys.argv[1])


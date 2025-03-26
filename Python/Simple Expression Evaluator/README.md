# Simple Expression Evaluator
## Instructions
To run the program, run main.py along with an expression i.e 3+4. If you have spaces in your expression, you must enclose the expression with quotes i.e "3 + 4".

To run some test cases, run test_cases.py with no arguments.


## Design
This program has two main functions.
One for implementing the Shunting Yard Algorithm to convert a given expression from infix notation to postfix notation.
Another for evaluating an expression in postfix notation.

The Shunting Yard Algorithm function implements a stack and queue to hold operators and outputs.

I made my own classes for exceptions, a stack, and a queue. I laso made a class to hold an operator, its precedence, and its association.

## Algorithms
The Shunting Yard Algorithm was created by Edsger Dijkstra. It converts an expression in infix notation to postfix notation, so it can be more easily read by computers that implement a call stack.
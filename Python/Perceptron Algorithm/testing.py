import numpy as np
import perceptron
import random


def binary_even_or_odd(learning_rate, epochs):
    # binary representation of numbers 0-15
    X = np.array([
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        ])
    # Even/Odd classifications // 0: Even, 1: Odd
    y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
    step_activation_test(X, y, learning_rate, epochs)


def step_activation_test(X, y, learning_rate, epochs):
    res = perceptron.run_perceptron(X, y, learning_rate, epochs, perceptron.activation)
    print('Prediction vs Actual: ', res[0])
    print('Accuracy: ', res[1])
    print()
    print()


def default_test():
    # Example dataset: Simple OR gate problem
    # Inputs (X) and expected outputs (y)
    X = np.array([[0, 0],
    [0, 1],
    [1, 0],
    [1, 1]])
    y = np.array([0, 1, 1, 1])
    # Define hyperparameters
    learning_rate = 0.1
    epochs = 10 # Number of training iterations
    res = perceptron.run_perceptron(X, y, learning_rate, epochs, perceptron.activation)
    print(res)
    print()
    print()

def xor_test():
    X = np.array([[0, 0],
    [0, 1],
    [1, 0],
    [1, 1]])
    y = np.array([0, 1, 1, 0])
    learning_rate = 0.3
    epochs = 100
    res = perceptron.run_perceptron(X, y, learning_rate, epochs, perceptron.activation)
    print(res)
    print()
    print()

def and_test():
    X = np.array([[0, 0],
    [0, 1],
    [1, 0],
    [1, 1]])
    y = np.array([1, 0, 0, 1])
    learning_rate = 0.3
    epochs = 100
    res = perceptron.run_perceptron(X, y, learning_rate, epochs, perceptron.activation)
    print(res)
    print()
    print()


def main():
    #default_test()
    #xor_test()
    #and_test()

    binary_even_or_odd(0.1, 10)
    binary_even_or_odd(0.2, 10)
    binary_even_or_odd(0.5, 10)

    binary_even_or_odd(0.1, 2)
    binary_even_or_odd(0.1, 3)


if __name__ == '__main__':
    main()
import numpy as np


def activation(x):
    """Step activation function."""
    return 1 if x >= 0 else 0


def predict(x, weights, bias, activation_method):
    """Calculate perceptron output for input x."""
    weighted_sum = np.dot(weights, x) + bias
    #print('WS:', weighted_sum)
    return activation_method(weighted_sum)


def train(X, y, weights, bias, learning_rate, epochs, activation_method):
    for epoch in range(epochs):
        total_error = 0
        for i in range(len(X)):
            # Forward pass: get prediction
            y_pred = predict(X[i], weights, bias, activation_method)
            # Calculate error
            error = y[i] - y_pred
            total_error += error**2
            # Update weights and bias
            weights += learning_rate * error * X[i]
            bias += learning_rate * error
        # Print epoch and error to monitor training
        print(f"Epoch {epoch+1}/{epochs}, Error: {total_error}")
    return weights, bias


def run_perceptron(X, y, learning_rate, epochs, activation_method):
    # Initialize weights and bias
    try:
        weights = np.random.rand(X.shape[1]) # Randomly initialize weights for variable amounts of inputs
    except Exception: # If input has only 1 input variable, X.shape[1] doesn't exist
        weights = np.random.rand(1)
    bias = np.random.rand(1) # Randomly initialize the bias
    
    # Train the perceptron
    weights, bias = train(X, y, weights, bias, learning_rate, epochs, activation_method)
    # Test the perceptron
    results = []
    accuracy = 0
    for i in range(len(X)):
        p = predict(X[i], weights, bias, activation_method)
        a = y[i]
        #status = 'Incorrect'
        if p == a:
            accuracy = ((accuracy * i) + 1) / (i + 1)
            #status = 'Correct'
        else:
            accuracy = (accuracy * i) / (i + 1)
        #print(f"Input: {X[i]}, Predicted: {p}, Actual: {a}, Status: {status}")
        results.append((p, a))
    return (results, accuracy)

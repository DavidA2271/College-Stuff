# Analysis
## Training
The perceptron definitely became more accurate with time. The amount of errors always wend down and not up. While testing I
saw that the first 7 or 8 epochs usually had one error, but the final predictions always had 100% accuracy.
## Limitations
I tried using and/xor datasets and the model's accuracy went down drastically. On most tests, it had and accuracy
of 50%. When theres only two options, 50% accuracy is not very good.
## Hyperparameters
Using the given dataset and the AND/XOR sets I wasn't able to really test the hyperparameters. The perceptron 
was always able to easily classify the OR dataset, and I never reached better accuracy with the AND/XOR sets
even after raising learning rate to 0.5 and epochs to 100.  
I made a different dataset that passes through 4 parameters and the perceptron has to classify if the parameters are
even or odd (i.e given [1, 0, 1, 0] which binary 1010 = 10 it must predict even or odd.)  
The perceptron was able to operate on it very well (I did modify some of the code). It seemed like it was always able to classify
an input as even or odd correctly after 3 epochs.
The perceptron with a 0.5 learning rate had considerable less errors than the perceptron with 0.1 learning rate.
## My Changes
I changed the code a bit to make it more versatile. I changed the predict method so that it could take an activation method as a parameter. I didn't end up making another activation method though.  
I added more parameters to a lot of functions so the X, y, learning rate, and epoch values could be played around with easier.  
I changed the code for initializing weights so it would use the shape of the input array. This allowed me to input a four value array as an input.  
I also added logic to calculate the accuracy of the perceptrons predictions.
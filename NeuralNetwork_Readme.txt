This is a mini Neural Network library with genetic algorithm methods also included.
Copy the NeuralNetwork.py folder to the Lib folder inside the python folder (to find the path, one can do import sys; sys.path).

In a program, to use NeuralNetwork library: 
--> import NeuralNetwork as nn

To declare a Neural Network,

--> dna = nn.NeuralNetwork(#inputs, #outputs, #hidden layers, #nodes in each hidden layer)

this initialises the neural network, with the given architecture. The default activation function used is tanh. To change it to sigmoid,

--> dna.Set_Activation('sigmoid')

The default learning rate is 0.01. To change it,

--> dna.Set_Learningrate(new rate) (Setting the learning rate high will give the opposite effect!!)

If we have a training data in the form:: inputs = [I1, I2, ...] (where In is one input (an array of length #inputs)) and targets = [T1, T2, ...], then to train the neural network, 

--> dna.Train(inputs, targets, epochs)

epochs are the number of times the same data set is iterated. If we do not pass any argument there, default is 10.

Now after training, if we want to predict the output of some input, 

--> dna.Guess(input)
This gives an array of length #outputs.

To get the loss/cost value at any point, call

--> loss = dna.Calc_Loss(input, target)


----Genetic Algorithm-----
In case we are using genetic algorithm to train the neural network, we might want to do a crossover/clone/mutate the dna based on fitness values.
The fitness function depends on the problem at hand, but crossover/clone/mutate are common to all genetic algorithms, hence they are part of this library.

To clone a neural network:

--> child = dna.Clone()
gives a new dna on which we can make changes without making changes on the parent

to mix the genetic material (weights and biases in this case!) of two parents say dna1 and dna2 (both having the same architecture)

--> child = dna1.crossover(dna2) OR child = dna2.crossover(dna1)
what it does is::
if dna1 has weights == [W12, W23, W34] where Wij means Weights from layer i to layer j, and dna2 has weights == [V12, V23, V34] then a random integer is picked from (0, length of weights). Say it is 1. Then the child gets a new set of weights, [W12, V23, V34]. Same for biases.

To mutate a dna;

--> dna.Mutate()
The default mutation rate is set to 0.01. To change it,
--> dna.Set_Mutationrate(new value)
based on the mutation rate, weights and biases may be modified by random numbers picked from a gaussian with mean 0 and standard deviation 0.1.

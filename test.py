import NeuralNetwork as nn
import numpy as np

test_x = [[0, 0, 0], [0, 0, 1],
		  [0, 1, 0],[1, 0, 0],
		  [1, 0, 1], [1, 1, 0],
		  [1, 1, 1]]

test_y = [[1, 0], [1, 0], [1, 0], [0, 1],[0, 1],[0, 1],[0, 1]]

NN = nn.NeuralNetwork(3, 2, 1, 4)

NN.Train(test_x, test_y, 1000)

for i in range(7):
	print(np.argmax(NN.Guess(test_x[i])))

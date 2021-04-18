from mlxtend.data import loadlocal_mnist
import NeuralNetwork as nn
import numpy as np

X, y = loadlocal_mnist(
        images_path='train-images.idx3-ubyte', 
        labels_path='train-labels.idx1-ubyte')
test_X, test_y = loadlocal_mnist(
        			images_path='t10k-images.idx3-ubyte', 
        			labels_path='t10k-labels.idx1-ubyte')
train_Y = []
train_X = X/255.0
for i in range(len(y)):
	a = np.zeros(10)
	a[y[i]] = 1
	train_Y.append(a)

test_X = test_X/255.0

NN = nn.NeuralNetwork(784, 10, 2, 128)
NN.Set_Learningrate(0.01)
NN.Set_Activation('tanh')

NN.Train(train_X, train_Y, 15)
correct = 0
for i in range(len(test_y)):
	guess = np.argmax(NN.Guess(test_X[i]))
	if guess == test_y[i]:
		correct += 1
percent = correct/len(test_y)
print(percent)

	

	





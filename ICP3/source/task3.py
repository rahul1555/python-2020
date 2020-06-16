#installing numpy from pip
import numpy as np
#giving a random vector of length 20
x = np.random.uniform(low=1, high=20, size=(20))
print(x)
#reshaping the vector in the size of(4,5)
y = np.reshape(x, (4, 5))
print(y)
#finding the maximum in the row and replacing it with zeros
indexes = np.arange(y.shape[0]), np.argmax(y, axis=1)
y[indexes] = 0
print(y)
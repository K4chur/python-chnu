import math
import numpy as np
import matplotlib.pyplot as plt


def yuikes(x):
    return 2 * x + math.sin(10 * x)


plt.xlabel('X')
plt.ylabel('Y')
plt.title('Y(x) = 2*x + sin(10x)  x=[-3...3]')

X = []
Y = []

for x in np.arange(-3, 3, 0.001):
    X.append(x)
    Y.append(yuikes(x))

plt.plot(X, Y)
plt.savefig('5_1.png')
plt.show()


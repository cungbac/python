import numpy as np
from matplotlib import pyplot as plt

b = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]
A = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]


plt.plot(A,b,'ro')

# Change row vectors to column vectors
A = np.array([A]).T
b = np.array([b]).T

# Create a square matrix
x_square = np.array([A[:,0]**2]).T

# Combine x_square and A
A = np.concatenate((x_square,A),axis=1)

# Create a cubed matrix
x_cubed = np.array([A[:,0]**3]).T

# Combine x_cubed and A
# A = np.concatenate((x_cubed,A),axis=1)

# Create a one vector
ones = [1 for i in range(len(A))]
ones = np.array([ones]).T

# Combine A and ones
A = np.concatenate((A,ones),axis=1)

# Use formula
x = np.linalg.inv(A.T.dot(A)).dot(A.T).dot(b)
print(x)

# Test data to draw
x0 = np.linspace(1,25,10000)
y0 = x[0][0]*x0*x0 + x[1][0]*x0 + x[2][0]
# y0 = x[0][0]*x0*x0*x0 + x[1][0]*x0*x0 + x[2][0]*x0 + x[3][0]

plt.plot(x0,y0)

plt.show()
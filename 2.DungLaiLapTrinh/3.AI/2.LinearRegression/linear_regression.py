import numpy as np
import matplotlib.pyplot as plt

A = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46]
b = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

ones = [1 for i in range(len(A))]
# ones = np.ones((A.shape[0],1),dtype= np.int8)

plt.plot(A,b,'ro')

A = np.array([A]).T
b = np.array([b]).T
ones = np.array([ones]).T
# ones = np.array([ones], dtype = np.int8).T

# concatenate A and 
A = np.concatenate((A,ones),axis = 1)

# Use formula
x = np.linalg.inv(A.T.dot(A)).dot(A.T).dot(b)

# Test data to draw
x0 = np.array([[1,30]]).T
y0 = x[0][0]*x0 + x[1][0]

x_test = 12
y_test = x_test*x[0][0] + x[1][0]

print(y_test)

plt.plot(x0,y0)
plt.show()
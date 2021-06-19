import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model

b = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46,42,39,31,30,28,20,15,10,6]
A = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

# Plot random data
plt.plot(A,b)

# Change row vectors to column vectors
A = np.array([A]).T
b = np.array([b]).T

# Create a square matrix
A_square = np.array([A[:,0]**2]).T

# Combine x_square and A
A = np.concatenate((A_square,A),axis=1)

# Create model
lr = linear_model.LinearRegression()
lr.fit(A,b)

# Coefficient and intercept
print(lr.coef_)
print(lr.intercept_)

# Plot parabole
x0 = np.linspace(1,25,10000)
y0 = x0**2*lr.coef_[0] + x0*lr.coef_[1] + lr.intercept_

plt.plot(x0,y0)
plt.show()
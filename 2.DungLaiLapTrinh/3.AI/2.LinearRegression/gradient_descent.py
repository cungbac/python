import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

def cost(x):
    m = A.shape[0]
    return 0.5/m * np.linalg.norm(A.dot(x) - b,2)**2

def grad(x):
    m = A.shape[0]
    return 1/m * A.T.dot(A.dot(x) - b)

# def gradient_descent(x_init, learning_rate, iteration):
#     x_list = [x_init]
#     for i in range(iteration):
#         x_new = x_init - learning_rate*grad(x_init)
#         x_list.append(x_new)
#         x_init = x_new
#     return x_list

def gradient_descent(x_init, learning_rate, iteration):
    x_list = [x_init]

    for i in range(iteration):
        x_new = x_list[-1] - learning_rate*grad(x_list[-1])

        # when to stop GD
        if np.linalg.norm(grad(x_new)) / len(x_new) < 0.5:
            break

        x_list.append(x_new)

    return x_list

# Raw data
A = np.array([[2,9,7,9,11,16,25,23,22,29,29,35,37,40,46]]).T
b = np.array([[i for i in range(2,17)]]).T

# Show raw data
fig1 = plt.figure('GD for Linear Regression',figsize=(12,6))
ax = plt.axes(xlim = (-10,60), ylim =(-1,20))
plt.plot(A, b,'ro')
# plt.show()

# Line created by Linear Regression formula
lr = linear_model.LinearRegression()
lr.fit(A,b)

print('intercept',lr.intercept_)
print('coefficient',lr.coef_,type(lr.coef_))

x0_gd = np.linspace(1,46,2)
y0_sklearn = lr.intercept_ + lr.coef_[0][0]*x0_gd

plt.plot(x0_gd,y0_sklearn)

# Add one to A
ones = np.ones((A.shape[0],1),dtype=np.int8)
A = np.concatenate((ones,A), axis = 1)

print(A)
# Random initial line
x_init = np.array([[1],[2]])
y0_init = x_init[0][0] + x_init[1][0]*x0_gd

#  y = b + ax
plt.plot(x0_gd,y0_init,color = 'red')
# print(x_init)
# print(x_init.shape)

# Rung gradient descent
iteration = 90
learning_rate = 0.0001

x_list = gradient_descent(x_init, learning_rate, iteration)

# Draw x_list (solution by GD)
for i in range(len(x_list)):
    y0_x_list = x_list[i][0] + x_list[i][1]*x0_gd
    # print(x_list)
    plt.plot(x0_gd,y0_x_list,color = 'black')
plt.show()

print(len(x_list))

# Draw cost per iteration to determine when to stop
cost_list = []
iter_list = []
for i in range(len(x_list)):
    iter_list.append(i)
    cost_list.append(cost(x_list[i]))

plt.plot(iter_list,cost_list)
plt.xlabel('Iteration')
plt.ylabel('Cost value')


plt.show()


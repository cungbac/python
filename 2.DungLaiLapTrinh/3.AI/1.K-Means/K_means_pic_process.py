# import packages
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import copy
from PIL import Image


# read image
img = plt.imread('pic1.jpg')
print(img[:10])
print(img.shape)

height = img.shape[0]
width = img.shape[1]

# reshape image to 2D list
img = img.reshape(height*width,3)

img2 = np.zeros_like(img)

# print(img.shape)

# K means
kmeans = KMeans(n_clusters=4).fit(img) # find clusters' coordinates
labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_

# update img
for i in range(len(img2)):
    img2[i] = clusters[labels[i]]

img3 = np.unique(img2)

print(len(img3))

# Restore origin shape
img2 = img2.reshape(height, width, 3)
img2 = Image.fromarray(img2)
img2.save('img2.jpg')

# for i in range(width):
#     for j in range(height):

# print(img2)
# Show image
fig = plt.figure(frameon=False)
ax = plt.Axes(fig, [0.,0.,1.,1.])
ax.set_axis_off()
fig.add_axes(ax)
plt.imshow(img2)
plt.show()

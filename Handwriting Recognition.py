# Handwriting recognition – Use of SKlearn clustering and KMeans machine learning model to predict numbers by reading handwriting
# Use of KMeans algorithm to predict numbers by reading handwriting

import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# give us a dataset of hand written digits
digits = datasets.load_digits()

# print(digits)
# random numbers and data

# print(digits.DESCR)

# :Number of Instances: 1797
# :Number of Attributes: 64
# :Attribute Information: 8x8 image of integer pixels in the range 0..16.
# 0 is white pixel, 16 is black

print("data is: ")
print(digits.data)
# list of lists

print("target is :")
print(digits.target)
# list of actuals digits which the data lists were supposed to represent

plt.gray()

plt.matshow(digits.images[100])

plt.show()

# prints the digits of image 100
print(" digits are :")
print(digits.images[100])

# prints the number of image 100
print(" The number is :")
print(digits.target[100])


# 10 different digits means there should be 10 different clusters, so k is 10
model = KMeans(n_clusters=10, random_state=42)

# fit data to model to form clusters
model.fit(digits.data)

# visualize centroids, adding a figure of size 8x3
fig = plt.figure(figsize=(8,3))

# style the visual
fig.suptitle("Cluster Center Images", fontsize=14, fontweight="bold")

# for loop to display each of the cluster centers

for i in range(10):
 
  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)
 
  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)

plt.show()


# Testing the model

# acquire data array for 4 numbers written on this website
# https://www.codecademy.com/paths/machine-learning-fundamentals/tracks/mle-unsupervised-learning-algorithms-i/modules/mle-k-means-clustering/projects/clustering

# prints out array that has digits data, (1996)

[
[0.00,0.00,0.00,2.28,1.06,0.00,0.00,0.00,0.00,0.00,0.00,6.86,3.81,0.00,0.00,0.00,0.00,0.00,0.00,6.86,3.81,0.00,0.00,0.00,0.00,0.00,0.00,6.86,3.81,0.00,0.00,0.00,0.00,0.00,0.00,6.70,4.79,0.00,0.00,0.00,0.00,0.00,0.00,5.48,5.33,0.00,0.00,0.00,0.00,0.00,0.00,3.80,3.80,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,1.13,4.57,4.34,2.19,0.08,0.00,0.00,0.00,4.49,7.31,6.92,7.62,2.20,0.00,0.00,0.00,4.57,6.86,5.17,7.62,1.97,0.00,0.00,0.00,3.18,6.78,7.00,7.62,1.52,0.00,0.00,0.00,0.00,0.00,2.05,7.62,1.44,0.00,0.00,0.00,0.00,0.00,2.96,7.62,0.53,0.00,0.00,0.00,0.00,0.00,3.04,7.62,0.00,0.00,0.00,0.00,0.00,0.00,1.97,5.63,0.00,0.00],
[0.00,1.36,4.34,5.33,5.33,3.87,0.00,0.00,3.19,7.54,7.31,5.78,6.93,7.24,0.00,0.00,7.54,5.39,0.53,0.00,5.33,7.62,0.53,0.00,7.62,4.33,1.29,0.30,6.39,7.62,0.76,0.00,5.16,7.62,7.62,7.62,7.62,7.62,0.76,0.00,0.00,0.98,2.66,3.05,4.03,7.62,0.76,0.00,0.00,0.00,0.00,0.00,3.04,7.62,0.68,0.00,0.00,0.00,0.00,0.00,1.66,5.10,0.30,0.00],
[0.00,0.00,0.76,4.64,5.33,2.73,0.00,0.00,0.00,0.76,6.47,7.24,5.41,2.73,0.00,0.00,0.00,5.86,7.62,3.26,0.00,0.00,0.00,0.00,1.29,7.62,7.54,7.15,0.76,0.00,0.00,0.00,3.04,7.62,2.11,7.38,5.02,0.00,0.00,0.00,3.05,7.62,2.89,6.69,6.01,0.00,0.00,0.00,1.36,6.61,7.61,7.38,1.89,0.00,0.00,0.00,0.00,0.00,0.75,0.45,0.00,0.00,0.00,0.00]
]

# pass data into kmeans algorithm
new_samples = np.array([
[0.00,0.00,0.00,2.28,1.06,0.00,0.00,0.00,0.00,0.00,0.00,6.86,3.81,0.00,0.00,0.00,0.00,0.00,0.00,6.86,3.81,0.00,0.00,0.00,0.00,0.00,0.00,6.86,3.81,0.00,0.00,0.00,0.00,0.00,0.00,6.70,4.79,0.00,0.00,0.00,0.00,0.00,0.00,5.48,5.33,0.00,0.00,0.00,0.00,0.00,0.00,3.80,3.80,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,1.13,4.57,4.34,2.19,0.08,0.00,0.00,0.00,4.49,7.31,6.92,7.62,2.20,0.00,0.00,0.00,4.57,6.86,5.17,7.62,1.97,0.00,0.00,0.00,3.18,6.78,7.00,7.62,1.52,0.00,0.00,0.00,0.00,0.00,2.05,7.62,1.44,0.00,0.00,0.00,0.00,0.00,2.96,7.62,0.53,0.00,0.00,0.00,0.00,0.00,3.04,7.62,0.00,0.00,0.00,0.00,0.00,0.00,1.97,5.63,0.00,0.00],
[0.00,1.36,4.34,5.33,5.33,3.87,0.00,0.00,3.19,7.54,7.31,5.78,6.93,7.24,0.00,0.00,7.54,5.39,0.53,0.00,5.33,7.62,0.53,0.00,7.62,4.33,1.29,0.30,6.39,7.62,0.76,0.00,5.16,7.62,7.62,7.62,7.62,7.62,0.76,0.00,0.00,0.98,2.66,3.05,4.03,7.62,0.76,0.00,0.00,0.00,0.00,0.00,3.04,7.62,0.68,0.00,0.00,0.00,0.00,0.00,1.66,5.10,0.30,0.00],
[0.00,0.00,0.76,4.64,5.33,2.73,0.00,0.00,0.00,0.76,6.47,7.24,5.41,2.73,0.00,0.00,0.00,5.86,7.62,3.26,0.00,0.00,0.00,0.00,1.29,7.62,7.54,7.15,0.76,0.00,0.00,0.00,3.04,7.62,2.11,7.38,5.02,0.00,0.00,0.00,3.05,7.62,2.89,6.69,6.01,0.00,0.00,0.00,1.36,6.61,7.61,7.38,1.89,0.00,0.00,0.00,0.00,0.00,0.75,0.45,0.00,0.00,0.00,0.00]
])

# use predict function to predict new labels for 4 digits
new_labels = model.predict(new_samples)

# use for loop to map out all data to digits 
# maps out each of the labels with the digits the algorithm thinks it represents
# for each digit from 0 to 4, print out the new labels number
print(" Is your number?: ")

for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')

# prints 7175 (needs to match the required handwriting more)
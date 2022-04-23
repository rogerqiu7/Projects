# Handwriting recognition – Use of SKlearn clustering and KMeans machine learning model to predict numbers by reading handwriting

import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# give us a dataset of hand written digits
digits = datasets.load_digits()

# print(digits)
# appears to be a list of arrays of numbers 
# targets that is an array of numbers
# images which are lists of arrays 

print(digits.DESCR)

# :Number of Instances: 1797
# :Number of Attributes: 64
# :Attribute Information: 8x8 image of integer pixels in the range 0..16.
# 0 is white pixel, 16 is black

print("data is: ")
print(digits.data)
# list of arrays that is the data

print("target is :")
print(digits.target)
# list of actuals digits which each list is supposed to represent

# visualize one of the digits using matshow which displays an array as matrix using a 2d array
# lets print the 100th data set
plt.gray()
plt.matshow(digits.images[100])
plt.show()
# appears to be a picture of the number 4

# prints the digits of image 100
print(" digits for this picture are :")
print(digits.images[100])
# larger numbers seem to be lighter areas on the image

# prints the number of image 100
print(" The number is :")
print(digits.target[100])
# image 100 is in fact a picture of the number 4


# 10 different digits here (0 to 9) means there should be 10 different clusters, so k (num_clusters) is 10
# The random_state will ensure that every time you run your code, the model is built in the same way. This can be any number.
model = KMeans(n_clusters=10, random_state=42)

# fit data to model to form clusters
model.fit(digits.data)

# start creating a multi chart to visualize centroids, start by adding a figure of size 8x3
fig = plt.figure(figsize=(8,3))

# style the visual
fig.suptitle("Cluster Center Images", fontsize=14, fontweight="bold")

# for loop to display each of the cluster centers
for i in range(10):
 
  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)
 
  # Display each image of the model at i location, reshaped and using a colormap setup
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)

plt.show()
# appears to be the images of the number 0 to 9


# Testing the model
# acquire data array for 4 numbers written on this website
# https://www.codecademy.com/paths/machine-learning-fundamentals/tracks/mle-unsupervised-learning-algorithms-i/modules/mle-k-means-clustering/projects/clustering
# go to the right panel and type: http://localhost:8000/test.html

# write 4 digits and click get array, I used 1996
# prints out array that has digits data

# (1996):
[
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,2.79,4.33,0.00,0.00,0.00,0.00,0.00,0.30,6.32,7.08,0.00,0.00,0.00,0.00,0.00,0.00,0.00,7.61,0.00,0.00,0.00,0.00,0.00,0.00,0.00,7.61,0.00,0.00,0.00,0.00,0.00,0.00,0.38,7.46,0.00,0.00,0.00,0.00,0.00,0.00,0.76,6.85,0.00,0.00,0.00,0.00,0.00,0.00,0.23,3.58,0.00,0.00,0.00],
[0.00,3.57,7.16,7.61,3.95,0.00,0.00,0.00,2.80,6.70,1.06,1.13,7.07,0.68,0.00,0.00,4.57,3.12,0.00,0.00,5.93,2.28,0.00,0.00,3.95,5.79,3.73,2.59,7.08,2.12,0.00,0.00,0.37,2.81,3.95,5.03,7.39,0.76,0.00,0.00,0.00,0.00,0.00,0.00,6.85,0.76,0.00,0.00,0.00,0.76,4.71,0.22,7.16,0.53,0.00,0.00,0.00,0.15,5.47,5.61,7.16,0.00,0.00,0.00],
[0.00,0.45,5.78,7.39,5.63,0.60,0.00,0.00,0.00,3.80,4.94,0.60,4.87,4.71,0.00,0.00,0.00,5.25,2.43,0.08,2.64,7.46,0.00,0.00,0.00,3.72,7.39,7.62,6.78,7.62,0.00,0.00,0.00,0.00,0.00,0.00,0.00,7.62,0.00,0.00,0.00,0.00,0.00,0.00,0.00,7.61,0.00,0.00,0.00,3.27,0.98,0.00,2.80,6.92,0.00,0.00,0.00,4.16,6.23,5.62,6.69,1.81,0.00,0.00],
[0.00,0.00,2.26,7.23,2.20,0.00,0.00,0.00,0.00,0.00,6.55,2.12,0.00,0.00,0.00,0.00,0.00,0.98,7.62,3.88,0.75,0.00,0.00,0.00,0.00,1.75,6.55,4.63,6.61,0.30,0.00,0.00,0.00,2.28,5.33,0.00,5.86,2.21,0.00,0.00,0.00,2.28,5.93,0.00,5.33,2.28,0.00,0.00,0.00,0.37,6.31,4.55,6.09,1.90,0.00,0.00,0.00,0.00,0.74,4.57,5.93,0.53,0.00,0.00]
]

# pass data as new smaples into kmeans algorithm
new_samples = np.array([
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,2.79,4.33,0.00,0.00,0.00,0.00,0.00,0.30,6.32,7.08,0.00,0.00,0.00,0.00,0.00,0.00,0.00,7.61,0.00,0.00,0.00,0.00,0.00,0.00,0.00,7.61,0.00,0.00,0.00,0.00,0.00,0.00,0.38,7.46,0.00,0.00,0.00,0.00,0.00,0.00,0.76,6.85,0.00,0.00,0.00,0.00,0.00,0.00,0.23,3.58,0.00,0.00,0.00],
[0.00,3.57,7.16,7.61,3.95,0.00,0.00,0.00,2.80,6.70,1.06,1.13,7.07,0.68,0.00,0.00,4.57,3.12,0.00,0.00,5.93,2.28,0.00,0.00,3.95,5.79,3.73,2.59,7.08,2.12,0.00,0.00,0.37,2.81,3.95,5.03,7.39,0.76,0.00,0.00,0.00,0.00,0.00,0.00,6.85,0.76,0.00,0.00,0.00,0.76,4.71,0.22,7.16,0.53,0.00,0.00,0.00,0.15,5.47,5.61,7.16,0.00,0.00,0.00],
[0.00,0.45,5.78,7.39,5.63,0.60,0.00,0.00,0.00,3.80,4.94,0.60,4.87,4.71,0.00,0.00,0.00,5.25,2.43,0.08,2.64,7.46,0.00,0.00,0.00,3.72,7.39,7.62,6.78,7.62,0.00,0.00,0.00,0.00,0.00,0.00,0.00,7.62,0.00,0.00,0.00,0.00,0.00,0.00,0.00,7.61,0.00,0.00,0.00,3.27,0.98,0.00,2.80,6.92,0.00,0.00,0.00,4.16,6.23,5.62,6.69,1.81,0.00,0.00],
[0.00,0.00,2.26,7.23,2.20,0.00,0.00,0.00,0.00,0.00,6.55,2.12,0.00,0.00,0.00,0.00,0.00,0.98,7.62,3.88,0.75,0.00,0.00,0.00,0.00,1.75,6.55,4.63,6.61,0.30,0.00,0.00,0.00,2.28,5.33,0.00,5.86,2.21,0.00,0.00,0.00,2.28,5.93,0.00,5.33,2.28,0.00,0.00,0.00,0.37,6.31,4.55,6.09,1.90,0.00,0.00,0.00,0.00,0.74,4.57,5.93,0.53,0.00,0.00]
])

# use predict function to predict new labels for 4 digits given our 4 samples
new_labels = model.predict(new_samples)



print("new labels: ")
print(new_labels)

# we have 3717 but from the earlier picture of all images, it seems that:
# Index 0 looks like 0
# Index 1 looks like 9
# Index 2 looks like 2
# Index 3 looks like 1
# Index 4 looks like 6
# Index 5 looks like 8
# Index 6 looks like 4
# Index 7 looks like 5
# Index 8 looks like 7
# Index 9 looks like 3

# since the clustered images are not indexed in order
# use for loop to match clustered handwriting images and their numbers with correct index 
# for each number from 0 to 4: 
# if the predicted new label is this number, print the corrected number out, and move to next number
# print(x, end='') so that all the digits are printed on the same line.
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

# prints 1595, close but needs to match the handwriting more
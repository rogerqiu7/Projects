# Differential Calculus Limits - A visual proof of limits by using functions to visualize convergence of derivatives
# Implementation of differentiation function from scratch and explore how it aligns with the limit definition of the derivative.
# Using matplotlib to check convergence of derivatives as h in (f(x+h) - f(x))/h approaches 0

import numpy as np
from math import sin, cos, log, pi
import matplotlib.pyplot as plt

# function that takes a mathematical function as input and uses the limit definition of a derivative to find the approximate derivate
# f: function to be differentiated 
# x: the point at which to differentiate f 
# h: distance between the points to be evaluated
def limit_derivative(f, x, h):
  
# compute the derivative at x with limit definition
  return (f(x+h) - f(x))/h

# f1(x) = sin(x)
def f1(x):
    return sin(x)

# f2(x) = x^4
def f2(x):
    return pow(x, 4)

# f3(x) = x^2*log(x)
def f3(x):
    return pow(x, 2) * log(x)

# Calculate derivatives here
# Using the limit_derivative() function, calculate the derivative of f3 at x=1 using the following values of h:

print("f3, 1, 2 is: ")
print(limit_derivative(f3, 1, 2))

print("f3, 1, .1 is: ")
print(limit_derivative(f3, 1, .1))

print("f3, 1, .00001 is: ")
print(limit_derivative(f3, 1, .00001))

# limit derivative appears to be approaching 1

# Using the limit_derivative() function, calculate the derivative of f2 at x=1 using the following values of h:

print("f2, 1, 2 is: ")
print(limit_derivative(f2, 1, 2))

print("f2, 1, .1 is: ")
print(limit_derivative(f2, 1, .1))

print("f2, 1, .00001 is: ")
print(limit_derivative(f2, 1, .00001))

# limit derivative appears to be approaching 4

# Using the limit_derivative() function, calculate the derivative of f1 at x=1 using the following values of h:

print("f1, 1, 2 is: ")
print(limit_derivative(f1, 1, 2))

print("f1, 1, .1 is: ")
print(limit_derivative(f1, 1, .1))

print("f1, 1, .00001 is: ")
print(limit_derivative(f1, 1, .00001))

# limit derivative appears to be approaching 0.54

# Graph the true derivative using plot_approx_deriv()

# f3 graph
print("f3 approaching 1 ")
# generate 200 samples between 1 and 10 
x_vals = np.linspace(1, 10, 200)
# use f3 function on all x values
y_vals = [pow(val,2) * log(val) for val in x_vals]
plt.figure(1)
plt.plot(x_vals, y_vals, label="True Derivative", linewidth=4)
plt.show()
plt.clf()

# limit derivative appears to be approaching 1

# f2 graph
print("f2 approaching 4")
# generate 200 samples between 1 and 10 
x_vals = np.linspace(1, 10, 200)
# use f2 function on all x values
y_vals = [4*pow(val,3) for val in x_vals]
plt.figure(1)
plt.plot(x_vals, y_vals, label="True Derivative", linewidth=4)
plt.show()
plt.clf()

# limit derivative appears to be approaching 4

# f1 graph
print("f1 approaching 0.54")
# generate 200 samples between 1 and 10 
x_vals = np.linspace(1, 10, 200)
# use f1 function on all x values
y_vals = [sin(val) for val in x_vals]
plt.plot(x_vals, y_vals, label="True Derivative", linewidth=4)
plt.show()
plt.clf()

# limit derivative appears to be approaching 0.54

# plot different approximated derivatives of f using limit definition of derivative
# set x values as 200 points between 1 and 10
# set h values at 10, 1, .25 and .01 to show convergence
def plot_approx_deriv(f):
  x_vals = np.linspace(1, 10, 200)
  h_vals = [10, 1, .25, .01]

# for values in h_vals, create derivative values from x values with the limit_derivative function from earlier
# derivative values will plot y points for our charts 
  for h in h_vals:
      derivative_values = []
      for x in x_vals:
          derivative_values.append(limit_derivative(f, x, h))
# plot x vals and new derivative values with each label h and its 4 values. 
      plt.plot(x_vals, derivative_values, linestyle='--', label="h=" + str(h) )
  plt.legend()
  plt.title("Convergence to Derivative by varying h")
  plt.show()

# prints the convergence of each function
print("f1 approaching 0.54")
plot_approx_deriv(f1)

# As the value of h gets closer to zero, the limit derivative of f1 approaches the true derivative of 0.54 calculated earlier
# This aligns with the limit definition of a derivative.

print("f2 approaching 4")
plot_approx_deriv(f2)

# As the value of h gets closer to zero, the limit derivative of f1 approaches the true derivative of 4 calculated earlier
# This aligns with the limit definition of a derivative.

print("f3 approaching 1")
plot_approx_deriv(f3)

# As the value of h gets closer to zero, the limit derivative of f1 approaches the true derivative of 1 calculated earlier
# This aligns with the limit definition of a derivative.

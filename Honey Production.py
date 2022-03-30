# Honey Production - Use of Simple Linear Regression machine learning model to predict honey production for future years

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# load the csv
df = pd.read_csv("honeyproduction.csv")
# print(df.head())

# Group years by average total production that year
# x axis has year, y axis has average production
# reset the index gives us list of intergers on left
prod_per_year = df.groupby("year").totalprod.mean().reset_index()
# print(prod_per_year)

# get a list of all the years
x = prod_per_year["year"] 
# print(x)

# rotates x into a 1-d array going down, now we have our x values
x = x.values.reshape(-1,1)
# print(x)

# get a list of all the average production
y = prod_per_year["totalprod"]
# print(y)

# plot the scatter chart
plt.scatter(x,y)
# plt.show()

# create the linear regression model
regr = linear_model.LinearRegression()

# feed x and y into the data
regr.fit(x,y)

# find the coefficient (slope) and intercept, coef needs 0 because it can be a list
print("Coef is " + str(regr.coef_[0]))
print("Intercept is " + str(regr.intercept_))

# predict y given x, using mx+b 
y_predict = regr.predict(x)
# print(y_predict)

# print linear regression with line of best fit
plt.plot(x,y_predict)
# plt.show()

# create future years
x_future = np.array(range(2013, 2050))
# print(x_future)

# reshape to 1d array 
x_future = x_future.reshape(-1,1)
# print(x_future)

# predict future year production y given future dates
future_predict = regr.predict(x_future)
# print(future_predict)

# comment out all previous plots to show final plot
plt.plot(x_future, future_predict)
plt.show()

# flatten function to turn arrays back to list
flattened_x = x_future.flatten()
flattened_y = future_predict.flatten()

# given year, predict production value
year = 2042
prod_by_year = np.interp(year, flattened_x , future_predict)
print("Production for year " + str(year) + " is " + str(prod_by_year))



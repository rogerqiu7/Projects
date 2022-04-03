# Honey Production - Use of Simple Linear Regression machine learning model to predict honey production for future years
# we are given a dataset (honeyproduction.csv) that shows honey production stats per state

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# load the csv
df = pd.read_csv("honeyproduction.csv")
print(df.head())

# Columns are:
# state, number of honey producing colonies, yield per colony, total production, stocks held by producers, average price per pound, value of production, year

# Group years by average total production that year
# x axis will have year, y axis has average production
# reset the index gives us list of integers on left
prod_per_year = df.groupby("year").totalprod.mean().reset_index()
# print(prod_per_year)
# prints out each year and its total production average

# get a list of all the years for our x axis
x = prod_per_year["year"] 
#print(x)

# rotates x into a 1-d array going down, now we have JUST our x values in a list
x = x.values.reshape(-1,1)
print("Reshaped Years: " + str(x))

# get a list of all the average production per year
y = prod_per_year["totalprod"]
print("prod per year: " + str(y))

# plot the scatter chart
plt.xlabel("Year")
plt.ylabel("Average Production")
plt.scatter(x,y)
plt.title("scatter of Given X and Y")
plt.show()

# now to use linear regression to predict future years
# create the linear regression model and set as regr
regr = linear_model.LinearRegression()

# feed x and y into the data using fit 
regr.fit(x,y)

# find the coefficient (slope) and intercept of regr, coef needs 0 because sometimes it can be a list
print("Coef is " + str(regr.coef_[0]))
print("Intercept is " + str(regr.intercept_))

# predict y (production) given x (year), using predict method as mx+b 
y_predict = regr.predict(x)
print("y_predict:" + str(y_predict))

# print linear regression with line of best fit to chart
plt.plot(x,y_predict)
plt.xlabel("Year")
plt.ylabel("Average Production")
plt.title("Line of Best fit from scatter chart")
plt.show()

# create future years
x_future = np.array(range(2013, 2050))
# print(x_future)

# reshape future years to 1d array 
x_future = x_future.reshape(-1,1)
# print(x_future)

# predicted future year productions y given future dates 2013 to 2050
future_predict = regr.predict(x_future)
# print(future_predict)

# plot scatter along with current and predicted future production line of best fit
# added a line in year 2042 to show predicted production
plt.plot(x,y_predict)
plt.xlabel("Year")
plt.ylabel("Average Production")
plt.scatter(x,y)
plt.plot(x_future, future_predict)
plt.axvline(2042, color="red", label="2042")
plt.title("Predicted future honey production")
plt.legend(loc=8)
plt.show()

# flatten function to turn arrays back to list so interp can read it
flattened_x = x_future.flatten()
flattened_y = future_predict.flatten()

# now to find the intersection point
# given year, predict production value
year = 2042
prod_by_year = np.interp(year, flattened_x , future_predict)
print("Estimated honey production for year " + str(year) + " is " + str(prod_by_year) + " pounds")
# estimated production is 892,970 pounds of honey


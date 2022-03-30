# Rent Prediction – Use of Multiple Linear Regression machine learning model to predict Manhattan rent prices given inputs

import pandas as pd

# import the dataset
streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

# view the data
df = pd.DataFrame(streeteasy)
# print(df.head())

# As with most machine learning algorithms, we have to split our dataset into:
# Training set: the data used to fit the model
# Test set: the data partitioned away at the very start of the experiment (to provide an unbiased evaluation of the model)
# In general, putting 80% of your data in the training set and 20% of your data in the test set is a good place to start.

from sklearn.model_selection import train_test_split

df = pd.DataFrame(streeteasy)

# set x as all of input values
x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]
print("x is ")
print(x.head())

# set y as all of output: rent
y = df[['rent']]
print("y is ")
print(y.head())

# split x into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

# show the shape of the x arrays
print("x_train array shape is ")
print(x_train.shape)
print("x_test array shape is ")
print(x_test.shape)


# show the shape of the rent
print("y_train array shape is ")
print(y_train.shape)
print("y_test array shape is ")
print(y_test.shape)

from sklearn.linear_model import LinearRegression

mlr = LinearRegression()

# fit in x train and y train arrays into this 3d arrray, .values so we remove header
mlr.fit(x_train.values, y_train.values)

# create new room with following criterias for attributes and features such as 1 bedroom, 1 bath, 620 sqft
predict_rent = [[2, 2, 1200, 10, 10, 50, 1, 0, 1, 0, 0, 1, 1, 0]]

# predict y (rent) given all of x values (apartment attributes)
predict = mlr.predict(predict_rent)

# sonnys predicted rent given y inputs, from x and y train fit
print("The predicted rent is: $%.2f" % predict)

import matplotlib.pyplot as plt

# plot scatters to show each of their correlation with price

plt.scatter(df[['size_sqft']], df[['rent']], alpha=0.4)
plt.title("sqft correlation with price")
plt.show()

plt.scatter(df[['bathrooms']], df[['rent']], alpha=0.4)
plt.title("bathrooms correlation with price")
plt.show()

plt.scatter(df[['bedrooms']], df[['rent']], alpha=0.4)
plt.title("bedrooms correlation with price")
plt.show()

plt.scatter(df[['floor']], df[['rent']], alpha=0.4)
plt.title("floor correlation with price")
plt.show()

plt.scatter(df[['building_age_yrs']], df[['rent']], alpha=0.4)
plt.title("building age correlation with price")
plt.show()

# 1. Use the `.corr()` method on `df` to get the correlation matrix 

import seaborn as sns

correlation_matrix = df.corr()

## Heatmap code:
red_blue = sns.diverging_palette(220, 20, as_cmap=True)
sns.heatmap(correlation_matrix, vmin = -1, vmax = 1, cmap=red_blue)
plt.show()


model=mlr.fit(x_train, y_train)

# predict y given x_test
y_predict = mlr.predict(x_test)

# view the tables
view_y_predict = pd.DataFrame(y_predict)
print("y predict is ")
print(view_y_predict.head())

view_y_test = pd.DataFrame(y_test)
print("y test is ")
print(view_y_test.head())

print("y_predict array shape is ")
print(y_predict.shape)

print("y_test array shape is ")
print(y_test.shape)

# plot actual vs predicted rent prices:
# x-axis is actual, y-axis is predicted

# plot y_tests vs y_predicts 
plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Actual Rent vs Predicted Rent")
plt.show()

#print out all 14 coefficients for all 14 variables
# print("The coefficients are " + str(mlr.coef_))

# evaluating accuracy using Residual Analysis:
# The difference between the actual value y, and the predicted value ŷ is the residual e.
# returns R^2, residual sum of squares divided by total sum of squares
# tells us variation in the y variable
# .77 means that all x variables together explain 77% variation in y.
# 3 x variables (sqft ft, bedrooms and age) might explain 95% of the variation in rent. 
# 1 is best possible, 0.7 is considered good. 

print("Train score:")
print(mlr.score(x_train, y_train))

print("Test score:")
print(mlr.score(x_test, y_test))


# residuals = predicted rent prices - actual rent prices
residuals = y_predict - y_test

# view residuals
view_residuals = pd.DataFrame(residuals)
print("residuals is ")
print(view_residuals.head())

plt.scatter(y_predict, residuals, alpha=0.4)
plt.xlabel("Predicted rent prices")
plt.ylabel("Residual amount")
plt.title('Residual Analysis')
 
plt.show()




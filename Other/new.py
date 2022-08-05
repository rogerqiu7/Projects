# Supplemental Policy
# We have our SQL query for a basic filter on individuals with certain credit score and debt to income but what if we were missing this information from a certain individual? What if an individual had a Debt to income ratio but not a credit score? How can we predict what is credit score will be based off of everyone else?
# This basic Linear Regression model allows us to find someones predicted credit score based off of their Debt to income ratio based off of a sample of about 6500 individuals.
# By finding their predicted credit score, we can use it for our analysis on whether or not this it would be safe to loan to this customer.

# import our libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# First lets set our X and Y axis of this model

# load the csv of the individuals from Mode dataset
df = pd.read_csv("mortgages.csv")
print(df.head())

# set x as the debt to income
x = df['debt_to_income_dti']
print("x is ")
print(x.head())

# set y as the credit score
y = df['borrower_credit_scoreat_origination']
print("y is ")
print(y.head())

# rotates x into a 1-d array, now we have our x values in a list
# Doing this allow us to input into a scatter chart
x = x.values.reshape(-1,1)
print("Reshaped debt to income ratio: " + str(x))

# do the same for the credit score 
y = y.values.reshape(-1,1)
print("Reshaped credit score: " + str(y))

# plot the scatter chart
plt.xlabel("Debt to Income")
plt.ylabel("Credit Score")
plt.scatter(x,y)
plt.title("Scatterchart of DTI and Credit Score")
plt.show()

# As you can see, without machine learning, it would be very difficult to find a trendline here

# Now lets use ML to find our linear regression and line of best fit based on this chart
# create the linear regression model and set as regr
regr = linear_model.LinearRegression()

# feed x and y into the data 
regr.fit(x,y)

# find the coefficient (slope) and intercept of regr, coef needs 0 because sometimes it can be a list
print("Coef is " + str(regr.coef_[0]))
print("Intercept is " + str(regr.intercept_))

# predict y (credit score) given x (DTI), using predict method as mx+b 
y_predict = regr.predict(x)
print("y_predict:" + str(y_predict))
# here is all our y values based on our x values

# lets create a line graph now of what the linear regression looks like based off of the predicted y values
# I also add a red horizontal line at a DTI of 10 to show where the credit score should be around for some with a DTI of 10.
plt.plot(x,y_predict)
plt.xlabel("Debt to Income")
plt.ylabel("Credit Score")
plt.axvline(10, color="red", label="Debt to Income of 10")
plt.legend(loc=7)
plt.title("Linear Regression of Credit Score to Debt to Income ratio")
plt.show()

# lets flatten x and y again so we can use in our final result
flattened_x = x.flatten()
flattened_y = y_predict.flatten()

# now lets use interp to find the exact credit score based on dti
# our predicted credit is based on given dti of 10, all the dti ratio's and all the predicted credit scores 
dti = 10 # enter any value here
credit = np.interp(dti, flattened_x, flattened_y)
print("Estimated DTI ratio at " + str(dti) + " would have a credit score at " + str(credit) + ".")
# based on the 6500 individuals, someone with a Debt to Income ratio of 10 would have a credit score of about 786
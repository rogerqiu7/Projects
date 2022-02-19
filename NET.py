# Cloudflare stock analysis
# 
# visualize data for the year of 2020:
# The distribution of the stock prices for the past year
# Cloudflare's earnings and revenue in the last four quarters
# The actual vs. estimated earnings per share for the four quarters in 2020
# A comparison of the Netflix Stock price vs Akamai (competitor) in 2020
# 
# During this project, I will analyze, prepare, and plot data. 
# The visualizations will help the asses the financial risk of the Cloudflare stock.
# 
# Financial Data Source: [Yahoo Finance](https://finance.yahoo.com)
# 
#
# Step 1
# 
# Import modules 

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


# Step 2

# load datasets and inspect.
# 
# In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. 
# This means this is the true closing stock price for a given business day.

cloudflare_stocks = pd.read_csv('NET.csv')
print()

akamai_stocks = pd.read_csv('AKAM.csv')
print()

cloudflare_stocks_quarterly = pd.read_csv('NET_daily_by_quarter.csv')
print()


# Step 3

#The year represented in the data is 2020, 
#The earliest date is 01-01-2020,
#The latest date is 01-01-2021
#The data in the NET and AKAM files are represented by month.
#The data in the cloudflare_stocks_quarterly file is represented by days through the 2020 year.
#The files are different in a matter of information, the cloudflare_stocks_quarterly is more detailed because it 
#contains the information from almost every trading day of the year.
#The Net and AKAM files contain information from the opening of the stock and closing of the stock from the month.
#The difference besides the summed information bewteen them is just one added column, the Quarter column.


# Step 4

print(cloudflare_stocks.head())


# Used Pandas to change the name of of the column of `Adj Close` to `Price` so that it is easier to work with the data and`inplace=True`.

akamai_stocks.rename(columns={'Adj Close': 'Price'}, inplace=True)
cloudflare_stocks.rename(columns={'Adj Close': 'Price'}, inplace=True)
cloudflare_stocks_quarterly.rename(columns={'Adj Close': 'Price'}, inplace=True)

print(cloudflare_stocks.head())
print(akamai_stocks.head())
print(cloudflare_stocks_quarterly.head())


# ## Step 5
# 
# data visualization
# 
# We want to get an understanding of the distribution of the Cloudflare quarterly stock prices for 2020. 
# Specifically, which quarter stock prices flucutated the most. 
# Can accomplish this using a violin plot with four violins, one for each business quarter.
# 
# 1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. 
# This will instantiate a figure and give us access to the axes through the variable name `ax`.
# 2. Use `sns.violinplot()` and pass in the following arguments:
# + The `Quarter` column as the `x` values
# + The `Price` column as `y` values
# + The `cloudflare_stocks_quarterly` dataframe as `data`
# 3. Improve the readability of the chart by adding a title of the plot. 
# Add `"Distribution of 2020 Cloudflare Stock Prices by Quarter"` by using `ax.set_title()`
# 4. Change `ylabel` to "Closing Stock Price"
# 5. Change `xlabel` to "Business Quarters in 2020"

plt.figure(figsize=(10,8))
ax = sns.violinplot(data=cloudflare_stocks_quarterly, x='Quarter', y='Price')
ax.set_title('Distribution of 2020 Cloudflare Stock Prices by Quarter')
plt.xlabel('Business Quarters in 2020')
plt.ylabel('Closing Stock Price')
plt.show()


# ## Step 6
# 
# Next, I will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. 
# will accomplish this using a scatter chart. 
# 
# 1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.
# 2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color
# 
# 3. Often, estimates and actual EPS are the same. To account for this, set  transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.
# 4. Add legend by using `plt.legend()` and passing in a list with two strings `["Actual", "Estimate"]`
# 
# 5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`


x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2020","2Q2020","3Q2020","4Q2020"]
earnings_actual =[-.06, -.04,-.03,-.02]
earnings_estimate = [-.10,-.06,-.06,-.05 ]
plt.scatter(x_positions, earnings_actual, color='red', alpha=0.5)
plt.scatter(x_positions, earnings_estimate, color='blue', alpha=0.5)
plt.legend(['Actual', 'Estimate'])
plt.xticks(x_positions, chart_labels)
plt.title('Earnings Per Share in Cents')
plt.show()


# ## Step 7

# Next, we will visualize the earnings and revenue reported by Cloudflare by mapping two bars side-by-side. 
# 
# plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand.
# 
# 1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars
# 2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data
# 3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars
# 4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data
# 5. Create a legend for  bar chart with the `labels` provided
# 6. Add a descriptive title for  chart with `plt.title()`
# 7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`


# The metrics below are in millions of dollars
revenue_by_quarter = [84, 91,100,114]
net_income_by_quarter = [-33, -26,-26,-34]
quarter_labels = ["1Q2020","2Q2020","3Q2020", "4Q2020"]

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars1_x = [t*element + w*n for element in range(d)]
plt.figure(figsize=(8,10))
plt.bar(bars1_x, revenue_by_quarter)


# Net Income
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars2_x = [t*element + w*n for element in range(d)]
plt.bar(bars2_x, net_income_by_quarter)


middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Net Income"]

plt.legend(labels)
plt.title('Visualization of Revenues and Net Income')
plt.xticks(middle_x, quarter_labels)
plt.xlabel('Quarters')
plt.ylabel('Revenue in Millions of Dollars')
plt.show()


# ## Step 8
# 
# will compare Cloudflare stock to Akamai stock in 2020. We will accomplish this by plotting two line charts side by side in one figure. 
# 
# Since `Price` which is the most relevant data is in the Y axis, I map  subplots to align vertically side by side.
# - Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot
#     - `1`-- the number of rows for the subplots
#     - `2` -- the number of columns for the subplots
#     - `1` -- the subplot you are modifying
# 
# - Chart the Cloudflare Stock Prices in the left-hand subplot. 
# Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. 
# - Assign "Cloudflare" as a title to this subplot. Hint: `ax1.set_title()`
# - For each subplot, `set_xlabel` to `"Date"` and `set_ylabel` to `"Stock Price"`
# - Chart the Akamai Stock Prices in the left-hand subplot. 
# Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. 
# - Assign "Akamai" as a title to this subplot. Hint: `plt.set_title()`
# - There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`


# Left plot Cloudflare
f = plt.figure(figsize=(13,6))
ax1 = plt.subplot(1, 2, 1)
plt.plot(cloudflare_stocks['Date'], cloudflare_stocks['Price'], color='red')
ax1.set_title('Cloudflare')
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price')
ax1.set_xticklabels(cloudflare_stocks['Date'], rotation=90)

# Right plot Akamai
ax2 = plt.subplot(1, 2, 2)
plt.plot(akamai_stocks['Date'], akamai_stocks['Price'], color='blue')
ax2.set_title('Akamai')
ax2.set_xlabel('Date')
ax2.set_ylabel('Stock Price')
ax2.set_xticklabels(akamai_stocks['Date'], rotation=90)
plt.subplots_adjust(wspace=0.2)

plt.show()
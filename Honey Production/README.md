# 🐝 Honey Production
## Use of Simple Linear Regression machine learning model to predict honey production for future years
- We have our dataset of honey production by different states for the last ~20 years. 
![image](https://user-images.githubusercontent.com/84350865/164947268-7591aa77-03dc-4c6b-8bc1-6d87a19a4538.png)
- Using pandas and numpy to find the mean production of each year, the data is re-arranged to total honey production and years as our X and Y data. 
- This data is displayed using a scatter chart
![image](https://user-images.githubusercontent.com/84350865/164947381-07546461-2501-4eda-ae40-e8694bb65112.png)
- Using SKlearn's linear regression function, we can find the line the best fit for our scatter: 
![image](https://user-images.githubusercontent.com/84350865/164947412-614b262c-8e17-4906-9881-bb88d4930ce5.png)
- Now that we have our line, we can extend to predict what honey production might be in 2042:
![image](https://user-images.githubusercontent.com/84350865/164947424-30aad2e5-a0d3-400d-b64b-3b519ac82d71.png)

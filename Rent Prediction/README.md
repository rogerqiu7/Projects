# 🏘️ Rent Prediction
## Use of Multiple Linear Regression machine learning model to predict Manhattan rent prices given inputs
- We have our dataset of thousands of apartments in Manhatten along with their features such as bedrooms, bathroom and building age:
![image](https://user-images.githubusercontent.com/84350865/164948085-2231a3b5-6227-4380-ac9f-d93f66ae5c0f.png)
- Used pandas to re-arrange the dataset so that rent price is our Y and all other features is our X:
![image](https://user-images.githubusercontent.com/84350865/164948111-d2098b6c-4714-4244-807f-4f07f45d33ec.png)
 - After feeding the linear regression function with our data, we can now enter our own X values in:
 ![image](https://user-images.githubusercontent.com/84350865/164948778-10572db2-0756-4888-a554-fddd0f4db8f6.png)
- The result: how much a 1200 sqft ft, 2 bedroom 2 bathroom apartment monthly rent would be in Manhatten
![image](https://user-images.githubusercontent.com/84350865/164948795-a07fc802-1d59-4970-8ed9-b316a3d8b4e6.png)
- We also broke our dataset into 20% test values to compare how it looks with our 80% training values:
- Our residual analysis shows predicted rent prices - actual rent prices

![image](https://user-images.githubusercontent.com/84350865/164948837-f708fe17-890e-432b-8c55-a2a50c335ec4.png)
![image](https://user-images.githubusercontent.com/84350865/164948846-7dfa771f-fab0-4bda-8dcb-099eea23cd69.png)

- Interesting correlations from the data:

![image](https://user-images.githubusercontent.com/84350865/164948805-dd6c292f-870e-4bce-84a9-4f825a55d8a4.png)
![image](https://user-images.githubusercontent.com/84350865/164948814-f191df3e-f99f-4289-8951-fa16dac4aa27.png)
![image](https://user-images.githubusercontent.com/84350865/164948816-3af023b0-46df-4a5b-ae47-5a3ffdda1a6d.png)
![image](https://user-images.githubusercontent.com/84350865/164948848-3aad81a6-c3f3-44ba-9564-e66fd83df951.png)


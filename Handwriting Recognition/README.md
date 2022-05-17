# ✏️ Handwriting recognition
## Use of KMeans clustering and SKlearn machine learning model to predict numbers by reading handwriting
- Dataset includes sets of numbers that are used to create a grayscale visual map that represents numbers
![image](https://user-images.githubusercontent.com/84350865/164949430-9536ffbc-b0d7-427a-8130-11ba9aa7ce78.png)
![image](https://user-images.githubusercontent.com/84350865/164949435-93429f86-f86e-4d1b-98d0-b352f2097ece.png)
- Using this dataset, we feed the KMeans cluster model, we visualize the clustered images represented by the data:
![image](https://user-images.githubusercontent.com/84350865/164949463-fc11a331-917b-4ba2-9306-1029612649b6.png)
- Now to test the the model, we acquire our own set of numbers based on our drawing using codecademy website:
![image](https://user-images.githubusercontent.com/84350865/164949673-4b821df6-b0e2-406a-a454-87703a11b4fe.png)
- Acquire the output and pass the data as new smaples in the KMeans model
![image](https://user-images.githubusercontent.com/84350865/164949683-e13778b3-95d7-4879-85a0-cfb0420f95dd.png)
- Since the images are not in indexed order, use a function to match clustered handwriting images and their numbers with the correct index:
- I wrote 1996, the result was 1595, close but my handwriting as slightly different than those in the model
![image](https://user-images.githubusercontent.com/84350865/164949725-969c1ba0-d9a8-44dc-b41b-04274b559628.png)




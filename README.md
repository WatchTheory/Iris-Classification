# Iris-Classification
This analysis the Iris dataset to classify species using scaled features using classification

## Problem 
- Analyze Iris dataset and apply feature scaling using StandardScaler.


## Data Dictionary

| Column       | Description                                                 |
| ------------ | ----------------------------------------------------------- |
| sepal_length | Length of the sepal of the flower (cm).                     |
| sepal_width  | Width of the sepal of the flower (cm).                      |
| petal_length | Length of the petal of the flower (cm).                     |
| petal_width  | Width of the petal of the flower (cm).                      |
| species      | Species of the iris flower (setosa, versicolor, virginica). |


## Summary

## Data Cleaning

No data cleaning had to be preformed on this dataset, no missing value, NaN values or special characters were present in the dataset, outliers were deteched 



### Key Visualization
This include key visualizations that highlight important aspects of the data. 


#### Visualization 1:
This pairplot shows the difference featueres for the petals and sepals. It shows the pairplot of each features

![pairplot](./images/iris_pairplot_2.png)


#### Visualization 2: 
This charts shows the distrubtion between species across the different flowers (setosa, versicolor, virginica)
![iris](./images/iris_chart_1.png)


#### Visualization 3: 
Lasly, this heatmap shows the correlation between the `sepal_length`, `sepal_width` and `petal_length`, `petal_width`.

As you can see from the heatmap, the strongest correlation is between petal witdh and petal height with `0.96` correlation.

![HeatMap](./images/heatMap.png)



## Conclusions/Recommendations

the dataset was trained on with the iris dataset 

- KNeighbors Regression
- Linear Regression
- Random Forest Regression

The result of the models 

| Model               | Accuracy |
| ------------------- | -------- |
| KNeighbors          | 0.82     |
| Linear Regression   | 0.79     |
| Random Forest       | 0.99     |

<br>

Here the best score here is the Random Forest was trained on the four features.



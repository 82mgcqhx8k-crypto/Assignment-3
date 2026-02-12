# Assignment-3

Purpose
This project aims to analyze measurements of iris flowers to understand the similarities and differences among the different species. 
By combining data on sepal and petal lengths/widths, performing basic data analyses like mean, median, and stanard deviation, and studying correlations.
The project provides insights into the features that distinguish each iris species. 

Class Design/Implementation
The main concept of the project revolves around the IrisData class. 
The class maintains attributes such as lists or arrays for sepal length, sepal width, petal length, and petal width.
Along with a names of species like setosa, versicolor, and virginica. These attributes store the raw data loaded from CSV files.
The class includes several methods to carry out the  analysis: 
The load_data() method reads the CSV files—specifically Petal_Data.csv and Sepal_Data.
The merge() method, well, merges the petal and sepal data based on a common( sample_id) ensuring that measurements from the same sample are aligned. 
The vaioud data analysis method that computes statistical metrics such as mean, median, and standard deviation for each feature across all species, 
While, also providing a summary of the data distribution and how it all correlates. 
Additionally, the correlations() method calculates correlation coefficients between feature pairs, revealing how strongly features are related to one another. 

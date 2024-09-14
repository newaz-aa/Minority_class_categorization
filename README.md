
# Minority-class Instance categorization

This repository contains the codes to classify minority class instances into certain categories depending on their complexity level. Details are discussed in the paper.

## Dependencies

This project uses the following libraries:

[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.1-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![pandas](https://img.shields.io/badge/pandas-2.1.0-blue?logo=pandas)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.26.0-blue?logo=numpy)](https://numpy.org/)

## Materials
* categorize_minority.py file contains the function to divide minority class instances into four categories: Safe, Border, Rare, and Outlier (depending on nearest neighbor rule)
* Minority-class instance categorization.ipynb file shows the use cases of the function on two datasets.





## categorize_minority.py


```bash
  Input: Data (Pandas DataFrame object)
  Output: An array showing the category of the minority class instances and the count.

  Optional input argument: No. of neighbours to consider (default=5)
```


## Paper

Proposed in the following article: 

Napierala, K. and Stefanowski, J., 2016. Types of minority class examples and their influence on learning classifiers from imbalanced data. Journal of Intelligent Information Systems, 46, pp.563-597.
## Screenshots

![App Screenshot](https://github.com/newaz-aa/Minority_class_categorization/blob/main/categorization.png)


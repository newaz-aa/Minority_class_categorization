
# Minority-class Instance categorization

This repository contains the codes to classify minority class instances into certain categories depending on their complexity level.

## Dependencies

This project uses the following libraries:

[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.1-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![pandas](https://img.shields.io/badge/pandas-2.1.0-blue?logo=pandas)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.26.0-blue?logo=numpy)](https://numpy.org/)

## Materials
* categorize_minority_v2.py => updated version
* categorize_minority.py => this file contains the function to divide minority class instances into four categories: Safe, Border, Rare, and Outlier (depending on the nearest neighbor rule)
* Minority-class instance categorization.ipynb => This file shows the use cases of the function on two datasets.




## categorize_minority.py


```
  Categorize minority-class samples by count of opposite-class neighbors.

   Parameters
   ----------
   data : DataFrame
       Features + label in one frame.
   minority_label : scalar
       The label value is considered "minority".
   n_neighbors: int
       # of neighbors to inspect.
   scale: bool
       Standardize features before KNN.
   mode: int
       1 => safe(0), pure(1–2), border(3–5)
       2 => safe(0–1), border(2–4), outlier(=5)
       3 => return raw g1..g6 buckets (0,1,2,3,4,>=5)
   custom_bins: dict or None
       If provided, overrides the mode. Example:
       {
         "s": [0],        # safe if 0
         "p": [1,2],      # pure if 1 or 2
         "b": [3,4],      # border if 3,4
         "o": "ge5"       # outlier if =5
       }
   feature_cols : list[str] or None
       If None, all columns except label_col are used.
   label_col: str or None
       If None, the last column is label.

   Returns
   -------
   minority_indices: np.ndarray
       Row indices of minority samples in `data`.
   groups: list
       Category label per minority index (same order).
   opp_counts: np.ndarray
       Opposite-class neighbor counts per minority sample (same order).
   """

```


## Paper

Newaz, A., Adib, A.U.R. and Jabid, T., 2024. iCost: A Novel Instance Complexity Based Cost-Sensitive Learning Framework. arXiv preprint arXiv:2409.13007.

Napierala, K. and Stefanowski, J., 2016. Types of minority class examples and their influence on learning classifiers from imbalanced data. Journal of Intelligent Information Systems, 46, pp.563-597.
## Screenshots

![App Screenshot](https://github.com/newaz-aa/Minority_class_categorization/blob/main/categorization.png)


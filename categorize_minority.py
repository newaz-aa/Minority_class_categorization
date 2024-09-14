# -*- coding: utf-8 -*-
"""
Created on Wed May  1 01:52:45 2024

@author: asifn
"""
# This function divides minority class instances into four categories: Safe, Border, Rare, and Outlier.

from sklearn.neighbors import NearestNeighbors
import numpy as np
import pandas as pd


def categorize_minority_class(data, n_neighbors=6):
    
    
    X = data.drop(data.columns[-1],axis=1)
    y = data[data.columns[-1]]
    ynp= np.array(y)
    
    knn = NearestNeighbors(n_neighbors=n_neighbors)
    knn.fit(X)
    
    minority_indices = np.where(y == 1)[0]
    distances, indices = knn.kneighbors(X.iloc[minority_indices,:])
    
    ysum=  np.sum(ynp[indices]==0, axis=1)
    
    out=[]
    for i in ysum:
        if i <2:
            out.append('s')
        elif i==2 or i==3:
            out.append('b')
        elif i==4:
            out.append('r')
        elif i>4:
            out.append('o')
            
    num_count= {'Safe': out.count('s'),
                'Border': out.count('b'),
                'Rare': out.count('r'),
                'Outlier': out.count('o')
               }
    return out, num_count

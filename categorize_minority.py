# -*- coding: utf-8 -*-
"""
Created on Wed May  1 01:52:45 2024

@author: asifn
"""

from sklearn.neighbors import NearestNeighbors
import numpy as np
import pandas as pd

#data=pd.read_csv(dataname)

def categorize_minority_class(data, n_neighbors=5):
    
    
    X = data.drop(data.columns[-1],axis=1)
    y = data[data.columns[-1]]
    ynp= np.array(y)
    
    knn = NearestNeighbors(n_neighbors=5)
    knn.fit(X)
    
    minority_indices = np.where(y == 1)[0]
    distances, indices = knn.kneighbors(X.iloc[minority_indices,:])
    
    ysum= n_neighbors - np.sum(ynp[indices], axis=1)
    
    out=[]
    for i in ysum:
        if i <2:
            out.append('s')
        elif i==2 | i==3:
            out.append('b')
        elif i==4:
            out.append('r')
        elif i==5:
            out.append('o')
    return out
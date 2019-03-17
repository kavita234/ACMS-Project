# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 23:09:00 2019

@author: ANJALI KUMARI
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('output.csv')
X = dataset.iloc[:, [0,1]].values

#using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init=10, random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('Determining number of clusters using elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('wcss')
plt.show()


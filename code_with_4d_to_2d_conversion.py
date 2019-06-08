# -*- coding: utf-8 -*-
"""
Created on Sat May 18 20:42:39 2019

@author: ANJALI KUMARI
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import sklearn
from sklearn import cluster
import random
import csv

a = int(0)
b = int(0)
line_count = int(0)
with open('output.csv', mode='w', newline='') as output:
    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Longitude","Latitude","Feedback","Frequency"])
with open('output1.csv', mode='w', newline='') as output:
    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Longitude","Latitude","Size"])
with open('input1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
            
            lat=int(row[3])
            lon=int(row[4])
            #print(lat," ",lon)
            
            i=0
            for i in range(0,70):
                la=(random.randrange(lat-50000,lat+50000, 1))/10000
                lo=(random.randrange(lon-50000, lon+50000, 1))/10000
                fe=random.randint(0,9)
                fr=random.randint(0,9)
                with open('output.csv', mode='a', newline='') as output:
                    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([lo, la, fe, fr])
                    a+=fe
                    b+=fr
                    line_count += 1

i=0
print(a)
print(b)
for i in range(0,300):
        la=(random.randrange(19000,30000))/1000
        lo=(random.randrange(68000, 83000))/1000
        fe=random.randint(0,9)
        fr=random.randint(0,9)
        a+=fe
        b+=fr
        line_count += 1
        with open('output.csv', mode='a', newline='') as output:
            writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([lo, la, fe, fr])
            


mean_feed = int(a/line_count)
mean_freq = int(b/line_count)
n = 0
with open('output.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        if n == 0 :
            n = 2
            continue
        la=row[0]
        lo=row[1]
        #print(lat," ",lon)
        fe=int(row[2])
        fr=int(row[3])
        
        
            
        with open('output1.csv', mode='a', newline='') as output:
            writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            size = (fe - mean_feed) + (fr - mean_freq) + 10
            writer.writerow([lo, la, size])
                    

# data_file = pd.read_csv('output.csv')
# longitude = data_file[1:,'Longitude']
# latitude = data_file[0:,1]
# feedback = data_file[0:,2]
# frequency = data_file[0:, 3]

#Applying silhoutte method to find optimal number of clusters
#wines = pd.read_csv('output1.csv', sep=',')
X_train = pd.read_csv('output1.csv', sep=',')
silhouette_score_values=list() 
NumberOfClusters=range(2,10)
 
for i in NumberOfClusters:
    
    classifier=cluster.KMeans(i,init='k-means++', n_init=10, max_iter=300, tol=0.0001, verbose=0, random_state=None, copy_x=True)
    classifier.fit(X_train)
    labels= classifier.predict(X_train)
    print ("Number Of Clusters:")
    print (i)
    print ("Silhouette score value")
    print (sklearn.metrics.silhouette_score(X_train,labels ,metric='euclidean', sample_size=None, random_state=None))
    silhouette_score_values.append(sklearn.metrics.silhouette_score(X_train,labels ,metric='euclidean', sample_size=None, random_state=None))
 
plt.plot(NumberOfClusters, silhouette_score_values)
plt.title("Silhouette score values vs Numbers of Clusters ")
plt.show()


Optimal_NumberOf_Components=NumberOfClusters[silhouette_score_values.index(max(silhouette_score_values))]
print ("Optimal number of components is:")
print (Optimal_NumberOf_Components)




print(mean_feed)
print(mean_freq)
print(line_count)


wines = pd.read_csv('output1.csv', sep=',')


size = wines['Size']
fill_colors = ['#FF9999']
edge_colors = ['red']

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=Optimal_NumberOf_Components, random_state=0).fit(wines)
print(kmeans.labels_)
kmeans.predict(wines)
print(kmeans.cluster_centers_)


plt.scatter(wines['Latitude'], wines['Longitude'], s=size, 
            alpha=0.4, color=fill_colors, edgecolors=edge_colors)
plt.plot(kmeans.cluster_centers_[:,1],kmeans.cluster_centers_[:,0],'k*')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Cluster with 4D objects in 2D',y=1.05)
plt.show()





#start here kavita code
# print(wines.shape)
# longitude = wines['Longitude']
# latitude = wines['Latitude']
# print(longitude)
# from sklearn.cluster import KMeans
# kmeans = KMeans(n_clusters=4, random_state=0).fit(wines)
# print(kmeans.labels_)
# kmeans.predict(wines)
# print(kmeans.cluster_centers_)



# LABEL_COLOR_MAP={0:'r',1:'b',2:'g',3:'y'}
# label_color=[LABEL_COLOR_MAP[l] for l in kmeans.labels_]

# plt.scatter(latitude,longitude,c=label_color)

# plt.plot(kmeans.cluster_centers_[:,1],kmeans.cluster_centers_[:,0],'k*')
# plt.xlabel ('Latitude')
# plt.ylabel ('Longitude')
# plt.title('Cluster')
# plt.show()
#end here
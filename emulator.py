
# coding: utf-8

# In[43]:


import numpy as np
import matplotlib.pyplot as plt
import random
import csv


with open('input1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
            
            lat=int(row[3])
            lon=int(row[4])
            #print(lat," ",lon)
            line_count += 1
            i=0
            for i in range(0,70):
                la=(random.randrange(lat-10000,lat+10000, 1))/10000
                lo=(random.randrange(lon-10000, lon+10000, 1))/10000
                with open('outjtu.csv', mode='a', newline='') as output:
                    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([lo, la])
i=0
for i in range(0,300):
        la=(random.randrange(19000,30000))/1000
        lo=(random.randrange(68000, 83000))/1000
        with open('outjtu.csv', mode='a', newline='') as output:
            writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([lo, la])


# In[46]:


data_file = np.loadtxt('outjtu.csv',delimiter=',')
longitude = data_file[:,0]
latitude = data_file[:,1]
#x=list(data_file)
#X = np.array(x)
print(data_file.shape)
print(longitude)
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4, random_state=0).fit(data_file)
print(kmeans.labels_)
kmeans.predict(data_file)
print(kmeans.cluster_centers_)

#plt.scatter(data_file[:, 0], data_file[:, 1], c=kmeans.labels_)

LABEL_COLOR_MAP={0:'r',1:'b',2:'g',3:'y'}
label_color=[LABEL_COLOR_MAP[l] for l in kmeans.labels_]

plt.scatter(latitude,longitude,c=label_color)
#print(kmeans.cluster_centers_[:,0])
#print(kmeans.cluster_centers_[:,1])
plt.plot(kmeans.cluster_centers_[:,1],kmeans.cluster_centers_[:,0],'k*')
plt.xlabel ('Latitude')
plt.ylabel ('Longitude')
plt.title('Cluster')
plt.show()


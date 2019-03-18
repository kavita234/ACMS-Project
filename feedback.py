import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import random
import csv


with open('output.csv', mode='w', newline='') as output:
    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Longitude","Latitude","Feedback","Frequency"])
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
                fe=random.randint(0,4)
                fr=random.randint(0,9)
                with open('output.csv', mode='a', newline='') as output:
                    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([lo, la, fe, fr])
i=0
for i in range(0,300):
        la=(random.randrange(19000,30000))/1000
        lo=(random.randrange(68000, 83000))/1000
        fe=random.randint(0,4)
        fr=random.randint(0,9)
        with open('output.csv', mode='a', newline='') as output:
            writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([lo, la, fe, fr])




# data_file = np.loadtxt('output.csv',delimiter=',')
# longitude = data_file[:,0]
# latitude = data_file[:,1]
# feedback = data_file[:,2]
# frequency = data_file[:, 3]



wines = pd.read_csv('output.csv', sep=',')

size = wines['Frequency']*wines['Feedback'] + 20
fill_colors = ['#FF9999']
edge_colors = ['red']

plt.scatter(wines['Latitude'], wines['Longitude'], s=size, 
            alpha=0.4, color=fill_colors, edgecolors=edge_colors)

plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Plotting 4D objects in 2D',y=1.05)
plt.show()





#start here kavita code
# print(data_file.shape)
# print(longitude)
# from sklearn.cluster import KMeans
# kmeans = KMeans(n_clusters=4, random_state=0).fit(data_file)
# print(kmeans.labels_)
# kmeans.predict(data_file)
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
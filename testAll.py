#from kmeans import kmeans
from pyIOUtils import readMatFile
from classifierTests import getLabelAccuracy
from sklearn.cluster import MeanShift, estimate_bandwidth,KMeans
from numpy import array
from RandProj import getProjected
from LLE import locally_linear_embedding
from SVDProj import getProjectedSVD
import time

def getPrecisionRecall(X,Y):

	X = array(X)
	#centroids,clusters = kmeans(X,15)
	start = time.time()
	kmeans = KMeans(init='k-means++', n_clusters=15, n_init=10)
	kmeans.fit(X)
	centroids = kmeans.cluster_centers_
	print getLabelAccuracy(centroids,X,Y),
	print time.time() - start,

	bandwidth = estimate_bandwidth(X)/1.5
	start = time.time()
	ms = MeanShift(bandwidth=bandwidth)
	ms.fit(X)
	centroids = ms.cluster_centers_
	print getLabelAccuracy(centroids,X,Y),
	print time.time() - start

locally_linear_embedding([[0,1],[1,2]],1 , 1)
print "Loading Dataset"
name = "data/all.mat"
A = array(readMatFile(name))
name = "data/labels.mat"
Y = array(readMatFile(name),dtype=int)-1
print "Data Loaded"
d=len(A[0])
t = 20
print "Full Data"
getPrecisionRecall(A,Y)
print "Projected"
Pr_A = getProjected(A,t)
getPrecisionRecall(Pr_A,Y)

print "LLE"
X_r, cost = locally_linear_embedding(A,50 , 50) 
getPrecisionRecall(X_r,Y)
print "SVD Projection"
#memory error above 5k
if len(A[0])>2000: 
	Pr_A = getProjectedSVD(getProjected(A,2000),50)
else: 
	Pr_A = getProjectedSVD(A,40)

getPrecisionRecall(Pr_A,Y)




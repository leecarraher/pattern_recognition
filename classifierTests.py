   
def dist(X,Y):
	'''
		Euclidean for now
	'''
	d = 0.0
	for i in xrange(len(X)):
		d=d+(X[i]-Y[i])*(X[i]-Y[i])
	return d
    

def classifier(centroids,data):
	'''
		Apply nearest centroid classifier to data
		returns nearest centroid idx and distance
	'''
	ret = [0]*len(data)
	retvals = [0.0]*len(data)
	for i in xrange(len(data)):
		mindist = dist(data[i],centroids[0])
		argmindist = 0
		for j in xrange(1,len(centroids)):
		    if dist(data[i],centroids[j]) < mindist:
		        mindist = dist(data[i],centroids[j])
		        argmindist = j
		ret[i] = argmindist
		retvals[i] = mindist
	return ret,retvals



def findlabels(Y,tildaY,k,labels):
	'''
		find which cluster has the most of a particular label
		return a mapping from cluster id->label
	'''
	counts = [ [0]*labels for i in range(k)]
	ret = {}
	for i in xrange(len(Y)):
		counts[tildaY[i]][Y[i][0]]+=1
	for i in xrange(k):
		clu = counts[i]
		mxlbl = clu[0]
		argmx = 0
		for ct in xrange(1,labels):
		    if clu[ct]>mxlbl:
		        mxlbl=clu[ct]
		        argmx = ct
		ret[i] = argmx
	# print counts
	return ret
  
def getLabelAccuracy(means,testX,testY):
	'''
	Compute the Precision Recall For labeled data
	'''
	k = len(means)
	ret,retvals = classifier(means,testX)

	labelMap = findlabels(testY,ret,len(means),len(testY))
	ctequal = 0
	#accumulate correct matches
	for i in range(len(testY)):
		ctequal += (testY[i]==labelMap[ret[i]])
	#print "Classification Accuracy:",
	return float(ctequal)/float(len(testY))


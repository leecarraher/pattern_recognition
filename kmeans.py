from random import shuffle,randint,random ,gauss
from copy import deepcopy


def dist(X,Y):
    '''
        Euclidean for now
    '''
    d = 0.0
    for i in xrange(len(X)):
        d=d+(X[i]-Y[i])*(X[i]-Y[i])
    return d
    
def least(q,D,fnc=dist):
    '''
        Find the index of the element in dataset @D that minimizes the function
        @fnc on query  @q
        Return the ArgLeast(fnc(q,D))
    '''
    l = fnc(q,D[0])
    lp = 0

    for i in xrange(1,len(D)):
        tmp=fnc(q,D[i])
        if tmp<l:
            lp = i
            l = tmp
    return lp
    


def assignClusters(A,means,clusters):
    '''
        assign to clusters
    '''
    swaps = 0
    newclusters = [list() for i in xrange(len(means))]
    for i in xrange(len(clusters)):
        for j in xrange(len(clusters[i])):
            arglst = least(A[clusters[i][j]],means)
            newclusters[arglst].append(clusters[i][j])
            swaps += int(arglst != i)
    return newclusters,swaps


def kmeansUpdate(A,clusters,dim):
    '''
        update means
    '''
    means  = []
    for cluster in clusters:
        mean=[0.0 for k in xrange(dim)]
        l = len(cluster)
        if l ==0:l=1
        for point in cluster:
            for d in xrange(dim):
                mean[d] = mean[d]+A[point][d] 
        for d in xrange(dim):mean[d] = mean[d]/float(l)
        means.append(mean)
    return means

def kmeans(A,k,maxiters = 1000):
    dim = len(A[0])
    #some data storage structures
    R = range(len(A))
    shuffle(R)
    clusters = []
    
    part = len(R)/k
    for i in xrange(k):
        clusters.append( R[i*part:(i+1)*(part)])
    means = kmeansUpdate(A,clusters,dim)
    clusters,swaps = assignClusters(A,means,clusters)
    while swaps>2 and maxiters>0:
        maxiters-=1
        means = kmeansUpdate(A,clusters,dim)
        clusters,swaps = assignClusters(A,means,clusters)
        #print "swaps = ",swaps
    return means, clusters

            
if __name__ == '__main__':
    pass
    #from numpy import array
    import sys
    k = 5
    dim = 200
    part = 500
    if len(sys.argv)>1:dim = int(sys.argv[1])
    if len(sys.argv)>2:part = int(sys.argv[2])
    if len(sys.argv)>3:k  = int(sys.argv[3])

    
    from pyIOUtils import *
    import os
    
    print "running kmeans on: ",
    print part,k
    
    rphashPR = []
    kmeansPR = []
    dimlist = []
    av = 20
    for h in xrange(1000,5000,500):
        
        
        rpAvg = []
        kmAvg = []
        for j in xrange(av):
            X , cntrs = getDataPoints(part,h,k)
            Y = [i/part for i in range(part*k) ]
        
            [trainX,trainY,testX,testY]=divide(X,Y,.50)
        
            #rphash
            writeMatFile(trainX, "X.mat")
            os.system("./test/test.out X.mat " + str(k))
            means = readMatFile("out.mat")
            rpAvg.append(getLabelAccuracy(means,testX,testY))
            
            
            #standard kmeans
            means,clusters = kmeans(trainX,k)
            kmAvg.append(getLabelAccuracy(means,testX,testY))
            
            
            del(X,Y,trainX,trainY,testX,testY)
            
        
        rphashPR.append(sum(rpAvg)/float(av))
        kmeansPR.append(sum(kmAvg)/float(av))
        dimlist.append(h)
        
        mrp = sum(rpAvg)/float(av)
        mkm = sum(kmAvg)/float(av)
        print h,mrp ,mkm,sum([x*x for x in rpAvg] )/av-mrp*mrp, sum([x*x for x in kmAvg] )/av-mkm*mkm
    
    print h
    print rphashPR
    print kmeansPR
        
    #assign centroid labels based on max labels from the training set
   
        


    


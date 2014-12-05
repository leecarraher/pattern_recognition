'''
Created on Jan 9, 2014

@author: lee
'''

def readMatFile(name):
    f = file(name,"r")
    x = int(f.readline())
    y = int(f.readline())
    M = [[0.0]*y for a in xrange(x)]
    
    for i in xrange(len(M)):
        for j in xrange(len(M[i])):
            M[i][j] = float(f.readline())
    f.close()
    return M

def writeMatFile(M,name):
    f = file(name,"w")
    f.write(str(len(M))+'\n')
    f.write(str(len(M[0]))+'\n')
    for i in xrange(len(M)):
        for j in xrange(len(M[i])):
            f.write(str(M[i][j])+'\n')
    f.close()
    return True


def divide(X,Y,split):
    '''
        Divide a dataset into training and testing under @split ratio
        @return: trainX,trainY,testX,testY
    '''
    n = len(X)
    mix=range(0,n)
    shuffle(mix)
      
    size = int(split*n)
      
    trainX = [0]*size
    trainY = [0]*size
    testX =  [0]*(n-size)
    testY =  [0]*(n-size)
      
    for i in range(0,size):
        trainX[i] = X[mix[i]]
        trainY[i] = Y[mix[i]]
      
    for i in range(size,n):
        testX[i-size] = X[mix[i]]
        testY[i-size] = Y[mix[i]]
    return [trainX,trainY,testX,testY]


CLUSTER_DISCREPANCY = 1.0 # makes visually acceptable clusters

def getDataPoints(part,d,clu):
    ret = [[] for j in xrange(part*clu)]
    clusterCenters = []
    #simulate different descriptor weightings
    varsDim = [random()*CLUSTER_DISCREPANCY for i in range(d)]
    for i in range(clu):
        #variance =CLUSTER_DISCREPANCY *(d**.5)
        means = [(random()*2.)-1.0 for b in range(d)] 
        clusterCenters.append(means)
        
        for j in range(part):
            p = [0]*d
            for k in xrange(d):
                p[k]= (gauss(0,varsDim[k])+means[k])
            ret[i*part+j]=p
    #from mean_shift import drawPts
    #drawPts(clusterCenters,ret)
    
    
    return ret,clusterCenters 


def dist(X,Y):
    d = 0.0
    for i in xrange(len(X)):
        d=d+(X[i]-Y[i])*(X[i]-Y[i])
    return d
    
def least(q,D):
    l = dist(q,D[0])
    lp = 0
    

    for i in xrange(1,len(D)):
        tmp=dist(q,D[i])
        if tmp<l:
            lp,l = i,tmp
    return lp,l
    


def assignClusters(Q,C):
  cost = 0.0
 
  for i in range(len(Q)):
    q = Q[i]
    assignment,cc = least(q,C)
    cost= cost + cc
    C[assignment].append(q)

  return C,cost


def centroid(Sprime):
  ss = [0.0]*len(Sprime[0])
  lSprime = len(Sprime)
  for vec in Sprime:
    for col in range(len(vec)):
      ss[col]=ss[col]+vec[col]/float(lSprime)
  return ss

def irredKMeans(Q,m,k,C,c,alpha,su):
  su = 0
  C.extend(c)
  #1
  if m ==0:
    C,cost = assignClusters(Q,C)
    su = cost+su
  #2
  t = range(0,len(Q))
  shuffle(t)
  S = [ [Q[t[i]] for i in range(int(1.0/float(alpha)))] for j in range(0,int(float(k)/(alpha**2)),int(1.0/float(alpha**2)))]
  for sprime in S:
    c = centroid(sprime)
    print c
    C = irredKMeans(Q,m-1,k,C,c,alpha,su)
  #3
  unsortedQ = []
  for q in Q:
    unsortedQ.append((least(q,C),q))

  unsortedQ.sort()

  U1 = [unsortedQ[u][1] for u in range(len(Q)/2)]
  U2 = [unsortedQ[u][1] for u in range(len(Q)/2),len(Q)]
  C,cost = assignClusters(U1,C)
  su = su +cost
  irredKMeans(U2,m,k,C,[],alpha,su)

  return C, cost
  

def kmeans(P,k,eps):
  C = []
  for i in range(k-1,k):
    C,cost = irredKMeans(P,i,i,C,[],eps/(64.0*k),0)
  return C

from numpy.random import randn,shuffle
P = randn(10000,10)

k = 10
eps = .1
kmeans(P,k,eps)

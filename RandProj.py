
from random import randrange
from numpy import *

def GenerateRand(n,t):
	return random.randn(n,t)/t**.5
	#M = [[] for i in xrange(t)];
	#r = 0
	#for i in xrange(t):
	#  for j in xrange(n):
	#	r = randrange(6)
	#	if r==0:M[i].append(j)
	#return M


def projectV(v,M,P,n,t):
	r=[]
	scale = (3.0/(n))**.5
	for i in xrange(t):
	  sum = 0.0
	  for j in P[i]:sum+=v[j]*scale
	  for j in M[i]:sum-=v[j]*scale
	  r.append(sum)
	return r

def getProjected(A,t):
	n = len(A[0])
	M = GenerateRand(n,t)
	return dot(A,M)
	#projectV(v,M)
	#P = GenerateRand(n,t)
	#Pr_A = []
	#for v in A:
	#	Pr_A.append(projectV(v,M,P,n,t))
	#return Pr_A

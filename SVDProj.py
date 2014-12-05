from numpy import *

def getProjectedSVD(A,t):
	U, s, Vh = linalg.svd(A,full_matrices=True)
	S = diag(s)
	#truncate the svd
	U = U[:,0:t]
	S = S[0:t,0:t]
	V = Vh[0:t,:]
	Pr_OptA = []

	return dot(dot(U,S),V)

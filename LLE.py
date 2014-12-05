from scipy.sparse import linalg, eye
from pyamg import smoothed_aggregation_solver
from sklearn import neighbors
import numpy as np
 
def locally_linear_embedding(X, n_neighbors, out_dim, tol=1e-6, max_iter=500):
	W = neighbors.kneighbors_graph(X, n_neighbors)
	 
	# M = (I-W)' (I-W)
	A = eye(*W.shape, format=W.format) - W
	A = (A.T).dot(A).tocsr()
	 
	# initial approximation to the eigenvectors
	X = np.random.rand(W.shape[0], out_dim)
	ml = smoothed_aggregation_solver(A)
	prec = ml.aspreconditioner()
	 
	# compute eigenvalues and eigenvectors with LOBPCG
	eigen_values, eigen_vectors = linalg.lobpcg(A, X, M=prec)
	 
	index = np.argsort(eigen_values)
	return eigen_vectors[:, index], np.sum(eigen_values)
  



from numpy import array
from scipy.linalg import svd
from numpy import dot
from numpy import diag 
A = array([[1, 2,1], [3, 4,2], [5, 6,4]])
print("matrix:\n",A)
U, s, VT = svd(A)
print("SVD")
print(U)
print(s)
print(VT)
Sigma=diag(s)
B=U.dot(Sigma.dot(VT))
print("Reconstructed Matrix:\n",B)
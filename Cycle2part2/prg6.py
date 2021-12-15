import numpy as np
a=np.array([[2,1,-2],[3,0,1],[1,1,-1]])
b=np.array([[-3],[5],[-2]])
print("A:",a)
print("B:",b)
x = np.linalg.solve(a, b)
print("Value of x:\n",x)
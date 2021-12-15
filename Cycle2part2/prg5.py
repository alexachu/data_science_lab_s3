import numpy as np
arr1 = np.array([[0, 2,9], [-2,0, 3],[-9,-3,0]])
print("Matrix:\n",arr1)
t= arr1.transpose()
print("Transpose of a matrix:\n",t)
comparison = arr1 == t
m1 = comparison.all()
m2=(arr1.transpose() == -arr1).all()
if m1 == True:
    print("symmetric")
else:
    print("Not symmetric")
if m2 == True:
    print("skew symmetric")
else:
    print("Not skew symmetric")
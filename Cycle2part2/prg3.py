import numpy as np
a = np.array([[1,2,5,6], [2,1,5,8],[1,6,5,9], [6,1,7,4]])
b = np.array([[2,3],[5,7]])
print("First matrix:\n",a)
print("Second matrix:\n",b)
x=a[2:,2:]
print(x)
y=b.dot(x)
print("Multiplied matrix:\n",y)
a[2:,2:]=y
print("Replaced matrix:\n",a)
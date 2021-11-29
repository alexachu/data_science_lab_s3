import math
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
disc=b * b - 4 * a * c
sol1= (-b+ math.sqrt(abs(disc))/2*a)
sol2= (-b- math.sqrt(abs(disc))/2*a)
if (disc>0):
    print("There are 2 real solutions:")
    print("solution 1:",sol1)
    print("solution 2:",sol2)
elif disc==0:
    print("There are 1 real solution:")
    print("solution is:", sol1)
elif disc<0:
    print("The roots are imaginary!!")


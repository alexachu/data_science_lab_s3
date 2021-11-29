def coprime(a,b):
    f=1
    for x in range(1,a+1):
        if a%x==0 and b%x==0:
            f=1
    return f==1
n1=int(input("Enter the First number:"))
n2=int(input("Enter the Second number:"))
if coprime(n1,n2):
    print("The given numbers are co-prime")
else:
    print("The given numbers are not coprime")
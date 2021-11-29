lower = int(input("Enter the lower interval: "))
upper = int(input("Enter the upper interval: "))
for num in range(lower,upper+1):
    if num>1:
        for m in range(2,num):
            if(num % m)==0:
                print(num)
                break


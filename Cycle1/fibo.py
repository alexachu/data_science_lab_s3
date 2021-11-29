n = int(input("How many terms? "))
fst=0
sec=1
count=0
if n==1:
    print(fst)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(fst)
        nth = fst + sec
        fst = sec
        sec = nth
        count += 1
i = int(input("enter a number:"))
orig = i
sum = 0 
while i>0:
    sum += (i % 10) **4
    i //= 10
if sum== orig:
    print("Armstrong Number") 
else:
    print("not an Armstrong number")
           
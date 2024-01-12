num = int(input("enter a word:"))
orig = num 
rev = 0
while num >0:
    rev = rev * 10 + num % 10
    num //= 10 
if rev == orig:
    print("palindrome")
else:
    print("not a palindrome")

#Reverse the Number
n = int(input("Enter the number : "))
rev = 0
while n > 0 :
    remainder = n % 10
    rev = (rev*10)+remainder
    n = n // 10
print("The Reversed number is ",rev) 

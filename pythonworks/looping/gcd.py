
        


a = int(input("Enter the first number >>> "))
b = int(input("Enter the second number >>> "))

gcd = 1

min=min(a,b)

for i in range(1, min + 1):  
    if a % i == 0 and b % i == 0:
        gcd = i  

print("The GCD of", a, "and", b, "is", gcd)





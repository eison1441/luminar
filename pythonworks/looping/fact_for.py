num=int(input("enter a number >>>"))

fact=1

for num in range(1,num+1):

    fact=fact*num

print(f"factorial of {num}={fact}")
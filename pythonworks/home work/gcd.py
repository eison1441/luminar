a=int(input("enter the first number >>>"))
b=int(input("Enter the second number >>>"))

while(b>0):
    r=a%b
    a=b
    b=r
print("GCD=",a)
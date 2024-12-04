num1=int(input("enter the first number>"))
num2=int(input("enter the second number>"))


print(f"Before swap a={num1},b={num2}")
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f"After swap a={num1},b={num2}")

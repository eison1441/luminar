num1=int(input("enter the 1st number >>>"))
num2=int(input("enter the 2ed number >>>"))

result=num1 if num1>num2 else num2
print("max=",result)

result2=num1 if num1<num2 else num2
print("min=",result2)
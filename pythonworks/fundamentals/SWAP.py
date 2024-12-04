a=100
b=200
print(f"Before swap a={a},b={b}")
a=a+b
b=a-b
a=a-b
print(f"After swap a={a},b={b}")
#logic1
# temp=a
# a=b
# b=temp

# logic2
# a=a+b
# b=a-b
# a=a-b

# logic 3
# a,b=b,a
# nter the number >>>"))
# real=num

# digit_count=len(str(num))

# print(digit_count)
# total=0

# while(num!=0):

#     digit=num%10

#     exponent=digit**digit_count


#     total=total+exponent
    
#     num=num//10

# if total==real:
#     print(f"{real} is a armstrong  number")
# else:
#     print(f"{real} is a not armstrong  number")



n=int(input("enter the number >>>"))

original=n

digit_count=len(str(n))

total=0

for i in range(1,n+1):
    if n!=0:
        digit=n%10
        exponent=digit**digit_count

        total=total+exponent

        n=n//10

if total==original:
    print(f"{original} is a armstrong number")

else:
    print(f"{original} is not a armstrong number")


        
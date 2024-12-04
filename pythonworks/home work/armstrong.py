

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


        
num=int(input("Enter the number >>>"))
real=num

digit_count=len(str(num))

print(digit_count)
total=0

while(num!=0):

    digit=num%10

    exponent=digit**digit_count


    total=total+exponent
    
    num=num//10

if total==real:
    print(f"{real} is a armstrong  number")
else:
    print(f"{real} is a not armstrong  number")
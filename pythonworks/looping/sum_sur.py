num=int(input("Enter the number >>>"))

total=0

while(num!=0):

    digit=num%10

    digit_sqr=digit**3

    total=total+digit_sqr
    
    num=num//10

print(total)
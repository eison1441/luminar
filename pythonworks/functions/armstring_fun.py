


def is_armstrong(number):
    real=number
    digit_count=len(str(number))

    total=0

    for i in range(1,number+1):
        if number!=0:
            digit=number%10
            exponent=digit**digit_count
            total=total+exponent
            number=number//10


    if total==real:
        print(f"{real} is a armstrong number")
    else:
        print(f"{real} is not a armstrong number")
        

is_armstrong(number=int(input("Enter a number >>>")))


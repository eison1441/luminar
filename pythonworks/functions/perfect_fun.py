

def is_perfect(num):
    

    total=0

    for i in range(1,num):

        if num%i==0:

            total+=i
    print("the number is perfect" if total==num else "the number is not a perfect number ")


is_perfect(num=int(input("Enter a number >>>")))
num=int(input("Enter the number >>>"))

is_prime="is a prime number"

for i in range(2,num):
    if num%i==0:
        is_prime="it is not a prime number "

        break
print(is_prime) 
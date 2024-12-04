
a = int(input("Enter the first number >>> "))
b = int(input("Enter the second number >>> "))


max_num=max(a,b)

for i in range(max_num,(a*b)+1,max_num):
    if i%a==0 and i%b==0:
        print(i)

        break
































# gcd = 1

# max

# for i in range(1, max(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         gcd = i


# lcm = (a * b) // gcd


# print("The LCM of", a, "and", b, "is", lcm)

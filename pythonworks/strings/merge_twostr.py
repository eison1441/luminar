# t1="PQRS"
# t2="ABCD"

# result=t1+t2

# print(result)




# t1="PQRSZW"
# t2="ABCD"
# result=''
# for i in range(len(t2)):
#     result += t1[i] + t2[i]

# print(result)




t1="PQRST"
t2="ABC"

smallest_text=t1 if t1<t2 else t2
largest_text=t1 if t1>t2 else t2

result=""

for i in range(0,len(smallest_text)):

    result+=t1[i]+t2[i]

balence_text=largest_text[len(smallest_text):]

result+=balence_text

print(result)
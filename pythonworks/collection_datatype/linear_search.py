# arr=[1,2,3,5,6,7,8,9]

# is_present=False

n=int(input("Enter the number to search >>>"))

# for i in range(0,len(arr)):
#     if n==arr[i]:
#         is_present=True
#         print(i+1)
#         break

# print(is_present)

# x=[8,6,4,2,3,5,1,7,9]
# for i in range(n-1):
#     for j in range(n-i-1):
#         if x[j]>x[j+1]:
#             t=x[j]
#             x[j]=x[j+1]
#             x[j+1]=t
# print(x)            

from array import*
x=array([])
print("how many elementsd")
n=int(input())
print("enter elements")
for i in range(n):
    x.append(int(input()))
for i in range(n-1):
    for j in range(n-i-1):
        if x[j]>x[j+1]:
            t=x[j]
            x[j]=x[j+1]
            x[j+1]=t
print(x)   


arr=[2,3,4,5,6,7,8,9]

print(arr)

sum=int(input("Enter the sum >>>"))

left=0


right=len(arr)-1

temp_sum=0

while(left<right):

    temp_sum=arr[left]+arr[right]

    if temp_sum==sum:
        print(arr[left],arr[right])
        break
    elif temp_sum>sum:
        right-=1
    elif temp_sum<sum:
        left+=1

# for printing all pairs

arr=[2,3,4,5,6,7,8,9]

print(arr)

sum=int(input("Enter the sum >>>"))

left=0


right=len(arr)-1

temp_sum=0

while(left<right):

    temp_sum=arr[left]+arr[right]

    if temp_sum==sum:
        print(arr[left],arr[right])
        left+1
        right-=1
    elif temp_sum>sum:
        right-=1
    elif temp_sum<sum:
        left+=1


arr=[2,3,4,5]
print(arr)

sum=int(input("Enter the sum >>>"))

temp_sum=0

for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        
        temp_sum=arr[i]+arr[j]

        if sum==temp_sum:
            print(arr[i],arr[j])
            break
        

    

    

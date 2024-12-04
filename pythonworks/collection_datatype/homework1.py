def missing_integer(arr):
    missing_int=1
    for i in arr:
        if i==missing_int:
            missing_int=missing_int+1
    return missing_int
arr=[1,2,3,4,5]
print(missing_integer(arr)) 

def missing_integer(arr):
    missing_int=1
    for i in arr:
        if i==missing_int:
            missing_int=missing_int+1
    return missing_int
arr=[1,2,4,5]
print(missing_integer(arr))


def missing_integer(arr):
    missing_int=1
    for i in arr:
        if i==missing_int:
            missing_int=missing_int+1
    return missing_int
arr=[1,3,4,5]
print(missing_integer(arr))


arr=[1,2,4,5,6]

arr.sort()

for i in range(0,len(arr)-1):
    j=i+1
    result=arr[j]-arr[i]
    if result!=1:
        print(arr[i]+1,"is missing")
    # if arr[i]-arr[j]==1:
    #     i+=1
    #     j=i+1
    # elif arr[i]-arr[j]!=1:
    #     print(arr[i])

    # duplicate number

arr=[1,2,2,2,1,4,5]
arr.sort()


duplicate_number=[]
for i in range(0,len(arr)-1):
    j=i+1

    result=arr[j]-arr[i]

    if result==0:
        if arr[i] not in duplicate_number:
            duplicate_number.append(arr[i])
print(duplicate_number)
        
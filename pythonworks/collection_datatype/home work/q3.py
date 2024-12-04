arr=[1,4,2,3,5]
arr.sort()
dupl=arr.copy()
for i in range(0,len(arr)-1):
    i=0
    j=i+1
    temp=arr[j]-arr[i]
    if temp==0:
        if arr[j] in dupl:
            ind=dupl.index(arr[j])
            dupl.pop(ind)
print(dupl[len(dupl)-2],"is the second largest element ")



arr1=[6,4,5,8,9,10]
arr2=[1,2,3,4,5]

arr1.sort()
arr2.sort()


p1=0
p2=0

while(p1<=len(arr1)-1 and p2<=len(arr2)-1):
    if arr1[p1]==arr2[p2]:
        print(arr1[p1])
        p1+=1
        p2+=1

    elif arr1[p1]<arr2[p2]:
        p1+=1

    elif arr1[p1]>arr2[p2]:
         p2+=1

        


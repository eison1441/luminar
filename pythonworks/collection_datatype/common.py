# arr1=[10,13,8,11,20,45]
# len1=len(arr1)
# arr2=[2,20,8,7,13,76,79,97]
# len2=len(arr2)
# count=0
# for i in range(len1):
#     for j in range(len2):
#         count+=1
#         if arr1[i]==arr2[j]:
          

# print(count)


arr1=[10,11,12,13,14,15]
arr2=[11,13,14,15,16]

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

        


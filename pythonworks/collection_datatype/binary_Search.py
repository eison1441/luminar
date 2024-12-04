arr=[10,8,7,12,13,20,25]
arr.sort()
search_element=int(input("Enter the element to search >>>"))
is_present="not in the array"
low=0
upp=len(arr)-1

while(low<=upp):
    mid=(low+upp)//2
    if search_element==arr[mid]:
        is_present="the number in the array"
        break
    elif search_element<arr[mid]:
        upp=mid-1
    elif search_element>arr[mid]:
        low=mid+1
print(is_present)




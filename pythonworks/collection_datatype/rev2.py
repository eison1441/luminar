arr=[100,200,300,400,500,600,700,800,900]
# odd_position_element.reverse().1000
# odd_position_element=[20,40,60]
# new_list=odd_position_element
# print(new_list)
# new_list.extend(arr)
# print(new_list)


# odd_position_element=[num for index,num in enumerate(arr) if index%2!=0]
# odd_position_element.reverse()

# print(odd_position_element)
# for index, in enumerate(odd_position_element):


left=1
right=len(arr)-1
if right%2==0:
    right-=1
while(left<right):
    
    arr[left],arr[right]=arr[right],arr[left]

    left+=2
    right-=2

print(arr)
     


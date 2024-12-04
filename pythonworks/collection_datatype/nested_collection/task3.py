lst1=["apple","mango","onion","pottato"]
lst2=[100,200]


result={}

for i in range(0,len(lst2)):
    list1_index_element=lst1[i]
    list2_index_element=lst2[i]
    result[list1_index_element]=list2_index_element
balance_element=lst1[len(lst2):]
for index,element in enumerate(balance_element):
    result[element]=index+1
print(result)
lst=[
    1,2,
    [10,20],
    [1,2,5,[10,3]],
    100
    ]

# lst2=str(lst)
# # print(lst2)
# # flatten_list=[num for ls in lst2 for num in ls]
# # print(flatten_list)

# max_char=[max(lst2)]
# print(max_char)

list_obj=[item for item in lst if isinstance(item,list)]
print(max(list_obj,key=len))
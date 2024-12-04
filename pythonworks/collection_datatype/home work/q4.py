
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']


count_dict = {}


for element in elements:
   
    if element in count_dict:
        count_dict[element] += 1
    else:
   
        count_dict[element] = 1


for key, value in count_dict.items():
    print(f"{key}: {value}")

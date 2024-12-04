# max
max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2
print(max_two("apple","kiwi"))

# min
min_two=lambda str1,str2:str1 if len(str1)<len(str2) else str2
print(min_two("apple","kiwi"))

# smart sub
smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
print(smart_sub(34,56))

# min_max_length_words

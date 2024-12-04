# from re import finditer

# text="I have 3 cars,2 bike and 1 cycle"
# pattern="[a-z]"
# num=finditer(pattern,text)
# for m in num:
   
#     print(m.start(),"==>",m.group())


# FOR ALL ALPHABETS(UP,LP)


# from re import finditer

# text="I have 3 cars,2 bike and 1 cycle"
# pattern="[a-z A-Z]"
# num=finditer(pattern,text)
# for m in num:
   
#     print(m.start(),"==>",m.group())





# FOR BOTH ALPHABETS AND THE NUMBERS


# from re import finditer

# text="I have 3 cars,2 bike and 1 cycle"
# pattern="[0-9a-zA-z]"
# num=finditer(pattern,text)
# for m in num:
   
#     print(m.start(),"==>",m.group())


# FOR BOTH UP,LP NUMBER AND SPACE"___"

# from re import finditer

# text="I have 3 cars,2 bike and 1 cycle"
# pattern="[0-9 a-zA-z]"
# num=finditer(pattern,text)
# for m in num:
   
#     print(m.start(),"==>",m.group())


# from re import finditer

# text="I have 3 cars,2 bike and 1 cycle"
# pattern="[^ A-Z0-9,ak]"
# num=finditer(pattern,text)
# for m in num:
   
#     # print(m.start(),"==>",m.group())


# from re import finditer

# text="I have 3 cars,2 bike and 1 cycle"
# pattern="[^A-Z0-9a-z]"
# num=finditer(pattern,text)
# for m in num:
   
#     # print(m.start(),"==>",m.group())


# from re import finditer

# text="I have 3 cars,2 bike and 1 cycle"
# pattern=r"\w"
# num=finditer(pattern,text)
# for m in num:
   
#     print(m.start(),"==>",m.group())




# from re import finditer

# text="I have 3 cars,2 bike and 1 cycle"
# pattern=r"\d"
# num=finditer(pattern,text)
# for m in num:
   
#     print(m.start(),"==>",m.group())



# from re import finditer

# text="I have 3 cars,2 bike and 1 cycle"
# pattern=r"\D"
# num=finditer(pattern,text)
# for m in num:
   
#     print(m.start(),"==>",m.group())


# from re import finditer

# text="I have 3 cars,2 bike and 1 cycle"
# pattern=r"\W"
# num=finditer(pattern,text)
# for m in num:
   
#     print(m.start(),"==>",m.group())


# from re import finditer

# text="I have 3 cars,2 bike and 1 cycle"
# pattern=r"\s"
# num=finditer(pattern,text)
# for m in num:
   
#     print(m.start(),"==>",m.group())

# from re import finditer

# text="I have 3 cars,2 bike and 1 cycle"
# pattern=r"\S"
# num=finditer(pattern,text)
# for m in num:
   
#     print(m.start(),"==>",m.group())

# from re import finditer

# text="I have 3 cars,2 bike and 1 cycle"
# pattern="\w+"
# num=finditer(pattern,text)
# for m in num:
   
#     print(m.start(),"==>",m.group())


# from re import finditer

# text="abababababbbbaaaaaababababab"
# pattern="a{2}"
# num=finditer(pattern,text)
# for m in num:
#     print(m.start(),"==>",m.group())


# from re import finditer

# text="abababababbbbaaaaaababababab"
# pattern="a{1,2}"
# num=finditer(pattern,text)
# for m in num:
#     print(m.start(),"==>",m.group())


from re import finditer

text="abababababbbbaaaaaababababab"
pattern="a*"
num=finditer(pattern,text)
for m in num:
    print(m.start(),"==>",m.group())
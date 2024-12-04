from re import finditer
path="C:\\Users\\ASUS\\Desktop\\pythonworks\\re file works\\re_file2.txt"

f=open(path,"r")

for line in f:
     hash=line.rstrip("\n")
     pattern="#\w+"
     matcher=finditer(pattern,hash)
     for m in matcher:
          print(m.group())
          




# from re import fullmatch
# f=open(path)
# content = f.read()
# words = content.split()

# for word in words:
#     pattern = r"[#]\w+"
#     match = fullmatch(pattern,word)

#     if match != None:
#         print(word)








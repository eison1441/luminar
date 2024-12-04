# from re import finditer
from re import findall
path="C:\\Users\\ASUS\\Desktop\\pythonworks\\re file works\\re_file3.txt"

f=open(path)

# for line in f:
#     link=line.rstrip("\n")
#     pattern="(http|https)://\w\S+"
#     matcher=finditer(pattern,link)
#     for o in matcher:
#         print(o.group())
# f.close() 

# pattern="https?://\w\S+"

content=f.read()
pattern="https?://[\w\S./]+"
url=findall(pattern,content)
for o in url:
    print(o)

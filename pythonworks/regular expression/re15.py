from re import findall
path="C:\\Users\\ASUS\\Desktop\\pythonworks\\re file works\\re_file4.txt"
f=open(path)
content=f.read()
pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"
date=findall(pattern,content)
for o in date:
    print("dates are ==>",o)
f.close()


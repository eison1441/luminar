from re import fullmatch
path="C:\\Users\\ASUS\\Desktop\\pythonworks\\re file works\\re_file1.txt"

f=open(path)

for line in f:
    phone=line.rstrip("\n")
    pattern="(91)?[0-9]{10}"
    matcher=fullmatch(pattern,phone)
    if matcher!=None:
        print("valid ==>",phone)
    else:
        print("invalid ==>",phone)
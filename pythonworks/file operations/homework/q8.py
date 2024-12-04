path="C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\homework\\q8.txt"
f=open(path,"r")
lst=[]
for line in f:
    line=line.rstrip("\n")
    line=line.split(" ")
    lst.extend(line)
cnt=lst.count("simple")
print(cnt)
f.close()
    
    
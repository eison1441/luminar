path="C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\homework\\q7.txt"
f1=open(path,"r")
for name in f1:
    name=name.rstrip("\n")
    reversed_string=name[::-1]
print(reversed_string)
f1.close()
 

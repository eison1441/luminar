 
path1="C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\homework\\words2.txt"
path2="C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\homework\\copy.txt"

f1=open(path1,"r")
f2=open(path2,"w")
for fn in f1:
    f2.write(fn)


f1.close()
f2.close()
path="C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\homework\\sentence.txt"

f1=open(path,"r")
for w in f1:
    words=w.split(" ")
    length=len(words)
print(words) 
print(length)   
f1.close()
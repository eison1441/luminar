f=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\fruits.txt","r")
fruits=[]
for line in f:
    fruits.append(line.rstrip("\n"))
print(fruits)
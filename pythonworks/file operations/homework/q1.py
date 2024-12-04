user_input=input("Enter a data >>>")
f1=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\homework\\words.txt","w")
f2=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\homework\\words.txt")

text=user_input
f1.write(text)



for w in f2:
    print(w)

f1.close()
f2.close()


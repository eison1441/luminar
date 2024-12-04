f=("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\words2.txt")
f1=("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\palindrome.txt")

f_read=open(f)
f_write=open(f1,"w")


for line in f_read:
    word=line.rstrip("\n")

    reversed_word=word[::-1]

    if word==reversed_word:
        f_write.write(word+"\n")
f_read.close()
f_write.close()


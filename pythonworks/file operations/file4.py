f=open("C:\\Users\\ASUS\\Desktop\\pythonworks\\datasets\\words.txt","r")
words=[]
for line in f:
    line=line.rstrip("\n")
    all_worlds=line.split(" ")
    for w in all_worlds:
        words.append(w)
# print(words)
count=0

words_dict={w:words.count(w) for w in words }

# print(words_dict)

# sorted_words=sorted(words_dict,key=lambda k:words_dict.get(k),reverse=True)
# print(sorted_words)

nested_word_dict=[[v,k] for k,v in words_dict.items() ]
print(sorted(nested_word_dict, reverse=True))
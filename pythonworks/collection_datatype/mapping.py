text=["apple","iphone","orange","potatto"]

vol=["a","e","i","o","u"]
vow=[word  for word in text if word[0] in vol]

print(vow)

con=[word  for word in text if word[0] not in vol]
print(con)

long=max([len(word)for word in text])
long_word=(word for word in text if len(word)==long)
print(long_word)
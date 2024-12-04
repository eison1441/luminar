w1="listen"
w2="silent"


is_anagram=True

w1=w1.casefold()
w2=w2.casefold()
for ch in w1:
    if ch not in w2:
        is_anagram=False
        break
print(is_anagram)
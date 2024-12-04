word=["hello","hello","hai","this","is","this","is","hello","hai"]
word_hz={w:word.count(w) for w in word}
print(word_hz)

rec_word=[k for k,v in word_hz.items() if v>1]
print(rec_word)

non_rec_word=[k for k,v in word_hz.items() if v==1]
print(non_rec_word)







# for w in word:
#     if w in word_count:
#         word_count[w]+=1
#     else:
#         word_count[w]=1
# print(word_count)



# PART TWO


text="ABABBCCDDE"
character_frequency={ch:text.count(ch) for ch in text}
print(character_frequency)
# for k,v in character_frequency.items():
#     if v==1:
    
#      print(k)
non_compri={k for k,v in character_frequency.items() if v==1}
print(non_compri)




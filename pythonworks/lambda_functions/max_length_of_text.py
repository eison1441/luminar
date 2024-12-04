text="this is is a a simple programming question to to find  find word word with maximum number of characters"
words=text.split(" ")


# print(max(words,key=lambda word:len(word)))



# def get_length(w):
#     return len(w)
# print(max(words,key=get_length))


# get_length=lambda word:len(word)

# srt_words=sorted(words,key=get_length,reverse=True)
# print(srt_words)

get_length=lambda word:words.count(word)
most_frequent_word=max(words,key=get_length)
print(most_frequent_word)


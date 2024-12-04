# min_max_length_words
words=["banana","apple","text","hello","hai"]

# print(max(words,key=lambda word:len(word)))

def get_length(word):
    return len(word)
max(words,key=get_length)
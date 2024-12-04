def most_frequent_word(text: str) -> str:
    text = text.lower()
    word_counts = {} 
    word = ''
    for char in text:
        if char.isalnum():  
            word += char
        else:
            if word: 
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
                word = ''  
    if word:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    most_common_word = None
    max_count = 0
    
    for word, count in word_counts.items():
        if count > max_count:
            most_common_word = word
            max_count = count
    return most_common_word
text = "Hello world! Hello everyone. Welcome to the world."
print(most_frequent_word(text))  

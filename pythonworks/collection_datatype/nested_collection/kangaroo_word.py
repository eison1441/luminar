# source_word="MADAM"

# target_word="MAD"




# source_index = 0
# target_index = 0


# for letter in source_word:
    
#     if target_index < len(target_word) and letter == target_word[target_index]:
#         target_index += 1  


# if target_index == len(target_word):
#     print(f"{target_word} is a kangaroo word contained in {source_word}.")
# else:
#     print(f"{target_word} is not a kangaroo word contained in {source_word}.")



source_word="CHEICKEN"

target_word="HEN"


character_count={ch:source_word.count(ch) for ch in source_word}

# for ch in source_word:
#     if ch in character_count:asdwasdwasfdsavcxzw
#         character_count[ch]+=1
#     else:
#         character_count[ch]=1

# print(character_count)
is_kangaroo="is a kangaroo word "
for ch in target_word:
    if ch in character_count and character_count.get(ch)>0:
        character_count[ch]-=1
    else:
        is_kangaroo="is not a kangaroo"
        break
print(is_kangaroo)
def vowels(text):
    v_count=0
    c_vount=0
    vowel="aeiouAEIOU"
    for ch in text:
        if ch in vowel:
            v_count+=1
        elif ch.isalpha():
            c_vount+=1
    print(f"vowels={v_count}")
    print(f"consonents={c_vount}")
   
vowels(text="eison")

# def vowels(text):
#     v_count = 0  # This counts the vowels
#     c_count = 0  # This counts the consonants

#     vowel = "aeiouAEIOU"  # Set of vowels (both lowercase and uppercase)
    
#     for ch in text:
#         if ch in vowel:
#             v_count += 1
#         elif ch.isalpha():  # Check if the character is a letter, i.e., a consonant
#             c_count += 1
    
#     # Output the counts for vowels and consonants
#     print(f"Vowels: {v_count}")
#     print(f"Consonants: {c_count}")

# # Call the function
# vowels(text="eison")

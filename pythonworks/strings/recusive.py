text="ABCABC"



seen_characters = []


for char in text:
    if char in seen_characters:
        
        print(f"The first recursive character is: {char}")
        break
    
    seen_characters.append(char)
else:
   
    print("No character is recursive.")

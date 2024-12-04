# text=input("Enter the text >>>")

# print(text.index("o"))

# find the username

# text=input("Enter the mailid >>>")


# find_index=text.index("@")

# print(f"{text[0:find_index]} Is the username!")


text="hellopython"

find_index=text.index("o")

add_text=text[find_index:]
reve_str=text[find_index-1::-1]

new_string=add_text+reve_str
print(new_string)



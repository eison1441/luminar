text=input("Enter the String >>>")

reversed_text=""

length=len(text)-1

for i in range(length,-1,-1):

    reversed_text+=text[i]

print(reversed_text)
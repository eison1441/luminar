from re import fullmatch
text=input("Enter the date ==>")

pattern="([1-9]|0[1-9]|1[0-2])"

matcher=fullmatch(pattern,text)
if matcher==None:
    print("invalid")
else:
    print("valid")

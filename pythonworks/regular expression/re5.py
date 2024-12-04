from re import fullmatch

user_input=input("Enter phonr number >>>")

pattern="(91)+\d{10}"

matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("invalid")
else:
    print("valid")
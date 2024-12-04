from re import fullmatch
email=input("Enter email id ==>")

patter="[a-z]+[a-z0-9]{5,63}@gmail.com"
matcher=fullmatch(patter,email)
if matcher==None:
    print("invalid")
else:
    print("valid")












# r"[a-z][\w.]{0,62}@gmail\.com"
# # "[a-z]{1}[\w]{63}@gmail.com"121
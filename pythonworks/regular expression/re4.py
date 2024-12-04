# starting with an alphabet p-t
# in second place mustbe a number  that is divisibile by 3
# any number aplabet @


from re import fullmatch

user_input=input("Enter a text ==>")

pattern="[p-tP-T][369][a-zA-z0-9@]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("invalid!!!!")
else:
    print("valid :) ") 
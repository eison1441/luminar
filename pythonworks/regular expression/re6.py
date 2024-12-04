# startwith KL
# 2 digit
# alphabets min=1 max= 2
# 4number


from re import fullmatch

text=input("Enter reg number >>>")

pattern="(KL)[0-73]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,text)

if matcher==None:
    print("invalid")
else:
    print("valid")


    # kl08bn4970



    
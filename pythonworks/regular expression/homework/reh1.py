# conditions: It should be eight characters long. The first character should be an uppercase alphabet. The next two characters should be a number, but the first character should be any number from 1-9 and the second character should be any number from 0-9.



from re import fullmatch

passport_number=input("Enter the passport number ==>")

pattern="[A-Z]{1}[1-9]{1}[0-9]{6}"

matcher=fullmatch(pattern,passport_number)

if matcher==None:
    print("invalid")
else:
    print("valid")
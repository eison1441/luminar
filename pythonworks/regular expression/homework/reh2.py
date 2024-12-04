# It should have 12 digits.
# It should not start with 0 and 1.
# It should not contain any alphabet and special characters.
# It should have white space after every 4 digits.

from re import fullmatch

aadhar=input("Enter the aadhar number ==>")

pattern="[2-9]{4} [0-9]{4} [0-9]{4}"

matcher=fullmatch(pattern,aadhar)

if matcher==None:
    print("invalid")

else:
    print("valid")
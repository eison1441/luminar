# pancard number
# 3 random alphabets upercase
# 4th place alphabet PCAFHT
# APPLICENT SIR NAME
# 4 digit
# 1alphabet

from re import fullmatch

pancard_number=input("Enter pancard number ==>")

pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pancard_number)

if matcher==None:
    print("invalid")
else:
    print("valid")
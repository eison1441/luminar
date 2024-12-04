# It should be 16 characters long, including space or hyphen (-).
# The driving license number can be entered in any of the following formats: DL-1420110012345 or DL14 2011001234512.
                                                                                                #1234 1234567891123
# The first two letters represent the code of the State in which the driving license is issued3.

from re import fullmatch

dl_number=input("Enter dl number ==>")

pattern="[A-Z]{2}[0-9]{2} [0-9]{4}[0-9]{7}"
matcher=fullmatch(pattern,dl_number)
if matcher==None:
    print("invalid")
else:
    print("valid")

    # r"(A-Z){2}{0-9}{2}[0-9]{4}[0-9]*"
    #  r"[A-Z]{2}\d{2}[A-Z]{1}\d{4}[0-9]*" 
    # "[A-Z]{2}[0-9]{2} [0-9]{4}[0-9]{7}"
    # r"[A-Z]{2}\d{2}[-\s][A-Z]\d{4}\d*"
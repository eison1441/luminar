def is_leap_year(year):
    if year<0:
        return False

    if (year%100!=0 and year%4==0) or (year%100==0 and year%400==0):
        return True
    else:
        return False
    

def test_is_leap_year():
    assert is_leap_year(2024)==True,"non century year chk faild!!"

    assert is_leap_year(2025)==False,"invalid non century year chk faild!!"

    assert is_leap_year(2000)==True,"century leap year chk faild!!"

    assert is_leap_year(1900)==False,"invalid  century year chk faild!!!"

    assert is_leap_year(-2000)==False,"invalid year chk faild!!!"

    # assert is_leap_year(-2004)==False,"-ve century leap year faild"

try:
    test_is_leap_year()
    print("test case passed")

except Exception as error:
    print("test case faild",error)

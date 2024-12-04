# 1800-2024
from re import fullmatch

text=input("Enter the year")
pattern="((18|19)[0-9]{2}|20[01][0-9]|202[0-4])"
matcher=fullmatch(pattern,text)
if matcher==None:
    print("invalid")
else:
    print("valid")


    # Boult Audio ZCharge Bluetooth Earphones with 40H Playtime, Dual Pairing Neckband, Zen™ ENC Mic, Type-C Fast Charging (10Mins=15Hrs), Biggest 14.2mm Bass Driver IPX5 Premium Silicone Neck Band (Blue)
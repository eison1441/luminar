weight_in_kg=int(input("Enter the weight in kg=>"))

height_in_cm=int(input("Enter the height in cm=>"))

height_in_meter=height_in_cm/100

BMI=weight_in_kg/height_in_meter**2 


BMI=round(BMI,1)


if BMI<18.5:
    print(f"{BMI} you are Underwight")

elif BMI>=18.5 and BMI<25:
    print(f"{BMI} you are normal wight")

elif BMI<30:
    print(f"{BMI} your overwight")

elif BMI>=30:
    print(f"{BMI} you are Obese")




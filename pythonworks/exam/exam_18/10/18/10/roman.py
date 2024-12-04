number = int(input("Enter a number between 1 and 15: "))
roman_numerals = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
    6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
    11: "XI", 12: "XII", 13: "XIII", 14: "XIV", 15: "XV"
}

if 1<=number<= 15:
    print("Roman numeral:", roman_numerals[number])
else:
    print("Number out of range")


# # Dictionary to map numbers to Roman numerals
# roman_numerals = {
#     1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
#     6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
#     11: "XI", 12: "XII", 13: "XIII", 14: "XIV", 15: "XV"
# }

# # Prompt the user for input
# number = int(input("Enter a number between 1 and 15: "))

# # Check if the input is valid
# if 1 <= number <= 15:
#     # Output the corresponding Roman numeral
#     print(f"The Roman numeral for {number} is: {roman_numerals[number]}")
# else:
#     # Handle invalid input
#     print("Number out of range. Please enter a number between 1 and 15.")

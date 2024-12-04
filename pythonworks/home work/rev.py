def reverse_number(number):
    reversed_number = 0
    while number > 0:
        last_digit = number % 10
       
        reversed_number = reversed_number * 10 + last_digit
        
        number = number // 10
    return reversed_number


num = int(input("Enter a number to reverse: "))
print("Reversed number:", reverse_number(num))

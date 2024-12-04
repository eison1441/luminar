def sum_of_digits(number):
    
    total_sum = 0
    
    
    number = abs(number)
    
    
    while number > 0:
        
        last_digit = number % 10
        total_sum += last_digit
        
        number //= 10
    
    return total_sum


user_input = int(input("Enter a number: "))


digit_sum = sum_of_digits(user_input)

print(f"The sum of the digits in {user_input} is {digit_sum}.")

def last_digit_max(num1,num2):

    
   num1_last_digit_max=num1%10

   num2_last_digit_max=num2%10

   print(num1 if num1_last_digit_max>num2_last_digit_max else num2)

last_digit_max(2342,2324)
arr=[10,20,30,40,2,3,7,8,9]
# cube={num:num**3 for num in arr}
# print(cube)

even_sqr={num:num**2 for num in arr if num%2==0}
print(even_sqr)
odd_cube={num:num**3 for num in arr if num%2!=0}
print(odd_cube)
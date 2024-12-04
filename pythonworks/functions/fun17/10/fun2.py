# second largest number 

def second_largest(*args):
    sorted_numbers=sorted(args,reverse=True)
    return sorted_numbers[1]

print(second_largest(10,20,30,40,124))
print(second_largest(10,20,30,40,12,200,1234))

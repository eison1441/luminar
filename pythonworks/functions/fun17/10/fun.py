# def add_numbers(*args):
#     print(args)
# add_numbers(10,20)
# add_numbers(10,20,30)



def product(*args):
    result=1
    for num in args:
        result=result*num
    return result
print(product(10,20))
print(product(10,20,30))
print(product(10,20,30,40))


def product(*args):

    return sum(args)
print(product(10,20))
print(product(10,20,30))
print(product(10,20,30,40))
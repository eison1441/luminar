def swap_dec(fn):
    def wrapper(n1,n2):
        
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper

def round_dec(fn):
    def wrapper(n1,n2):
        n1=round(n1)
        n2=round(n2)
        
        return fn(n1,n2)
    return wrapper




@swap_dec
@round_dec
def add_number(num1,num2):
    return num1+num2
@swap_dec
@round_dec
def sub_num(num1,num2):
    return num1-num2
@swap_dec
@round_dec
def div_num(num1,num2):
    return num1/num2

# def multi_num(num1,num2):
#     return num1*num2

print(div_num(2.3,10))
# print(add_number(4,24))
print(sub_num(4.7,34))
print(add_number(2.5,3.6))
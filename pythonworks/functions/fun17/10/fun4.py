# def calculator(*args,**kwargs):

#     if kwargs.get("operation")=="+":
#         return sum(args)
#     if kwargs.get("operation")=="*":

#         result=1
#         for num in args:
#             result=result*num

#         return result

# print(calculator(10,20,30,operation="+"))
# print(calculator(10,20,30,operation="*"))




def student_info(*args,**kwargs):
    if kwargs.get("operation")==("avg"):
    
        return sum(args)/len(args)
    if kwargs.get("operation")==("total"):
        return sum(args)
    if kwargs.get("operation")==("min"):
        return min(args)
    if kwargs.get("operation")==("max"):
        return max(args)
    


print(student_info(42,23,33,operation="avg"))
print(student_info(42,23,33,operation="total"))
print(student_info(42,23,33,operation="min"))
print(student_info(42,23,33,operation="max"))
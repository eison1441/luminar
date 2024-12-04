def sort_numbers(*args,**kwargs):
    if kwargs.get("reverse")=="True":
        return sorted(args,reverse=True)
    if kwargs.get("reverse")=="False":
        return sorted(args)
    

print(sort_numbers(10,4,6,2,56,7,23,5,reverse="True"))
print(sort_numbers(10,4,6,2,56,7,23,5,reverse="False"))
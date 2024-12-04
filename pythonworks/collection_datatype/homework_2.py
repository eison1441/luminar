def missing_integer(arr):
    missing_int=1
    for i in arr:
        if i==missing_int:
            missing_int=missing_int+1
    return missing_int
arr=[1,2,3,4,5]
print(missing_integer(arr)) 


def missing_integer(arr):
    missing_int=1
    for i in arr:
        if i==missing_int:
            missing_int=missing_int+1
    return missing_int
arr=[1,2,4,5]
print(missing_integer(arr))


def missing_integer(arr):
    missing_int=1
    for i in arr:
        if i==missing_int:
            missing_int=missing_int+1
    return missing_int
arr=[1,3,4,5]
print(missing_integer(arr))

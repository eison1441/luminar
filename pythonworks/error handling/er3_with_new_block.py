def review(rating):
    if rating<0:
        raise Exception("too low!!!!")
    
    elif rating>10:
        raise Exception("too high!!!!")

    else:
        print("Done!")
        
try:
    review(12)
except Exception as e:
    print("ERROR OCCURED!!!!!!-->",e)

print("hai")
print("hlo")

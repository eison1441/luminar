def review(rating):
    assert rating>0,"too low"
    assert rating in range(0,11),"too high"
    print("rated")

try:
    review(12)
     
except Exception as error:
    print("ERROR OCCURED!!!!!!-->",error)

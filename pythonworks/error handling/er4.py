def poll(age):
    assert age>18,"invalid age"
    print("voted")
try:
    poll(10)

except Exception as error:
    print("ERROR OCCURED!!!!!!-->",error)
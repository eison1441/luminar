user_input=input("enter a bracket pairs >>>")
# bracket=["{}","()","[]"]
# if user_input==bracket:
#     is_valid=True
# else:
#     is_valid=False

# print(is_valid)

# bracket={"{":"}","(":")","[":"]"}


bracket_pairs={"{":"}","(":")","[":"]","<":">"}
symbol_stack=[]
is_valid=True
top=-1
for symbol in user_input:
   
    
    if symbol in bracket_pairs:
        top=top+1
        symbol_stack.append(symbol)
    elif top==-1:
        is_valid=False
    elif symbol==bracket_pairs.get(symbol_stack[top]):
        top=top-1
        symbol_stack.pop()
    
       
    else:
        is_valid=False
if len(symbol_stack)==0 and is_valid==True:
    print("valid")
else:
    print("in valid")


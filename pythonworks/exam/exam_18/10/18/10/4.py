
# def palindrom(str):

#     length=len(str)
    
    
#     reverse=str[::-1]
#     if reverse==str:
#         print("palindrom")
        
#     else:
#         print("not palindrome")
    
        
#     # print(reverse)
    
#     # print("pal" ")
# print(palindrom(str="malayalam"))

def palindrom(s):
    reverse = s[::-1]  # Reverse the string
    if reverse == s:
        print("Palindrome")
    else:
        print("Not Palindrome")
palindrom("malayalm")
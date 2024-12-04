def palindrome(s):
    reverse=s[::-1]
    if reverse==s:
        print("palindrome")
    else:
        print("not palindrome")
palindrome("malaylam")
# def isPalindrome(string):
#     return string ==string[::-1]

# input = str(input("enter the string : "))
# if(isPalindrome(input)):
#     print("palindrome")
# else:
#     print("not palindrome")


###############################################
# str = "appa"

# if(str==str[::-1]):
#     print("palindrome")
# else:
#     print("not palindrome")
##############################################

def reverseString(string):
    str = ""
    for i in string:
        str = i + str
    return str

inp_string = str(input("enter the string : "))
if(inp_string== reverseString(inp_string)):
    print("palindrome")
else:
    print("not a palindrome ")

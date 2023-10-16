def reverseString(string):
    str = ""
    for i in string:
        str = i + str
    return str

inp_string = str(input("enter the string : "))
print(reverseString(inp_string))
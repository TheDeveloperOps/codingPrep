def remove_vowels(string):
    newString = ""
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for i in string:
        if i not in vowels:
            newString=newString+i
    print(newString)
#################### CONSONANTS ##############
def printConsonants(string):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    for i in string:
        if i not in vowels:
            print(i)
            count = count+1
    print("number of consonants in the string : "+str(count))
################### VOWELS #################
def printVowels(string):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    for i in string:
        if i in vowels:
            print(i)
            count = count+1
    print("number of vowels : "+str(count))
string = str(input("Enter string to perform string operations : "))
printVowels(string)
printConsonants(string)
remove_vowels(string)
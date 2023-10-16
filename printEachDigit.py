def printEachDigit(num):
    while num>0:
        y = num%10
        print(y)
        num = num//10
num = int(input("enter the number : "))
printEachDigit(num)
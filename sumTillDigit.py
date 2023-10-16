def sumOfDigit(num):
    sum =0
    while num>0:
        y = num %10
        sum = sum+y
        num = num//10
    return sum
def sumTillDigit(num):
    while(num>9):
        num = sumOfDigit(num)
    print(num)
num = int(input("enter the value : "))
sumTillDigit(num)
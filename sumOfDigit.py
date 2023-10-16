def sumOfDigit(num):
    sum = 0
    while num>0:
        y = num%10
        sum = sum+y
        num = num//10
    print(sum)
num = int(input("enter the number ; "))
sumOfDigit(num)
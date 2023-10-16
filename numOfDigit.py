def numOfdigt(num):
    count = 0
    while (num>0):
        count = count+1
        num = num//10
    print(count)
num = int(input("enter the number : "))
numOfdigt(num)

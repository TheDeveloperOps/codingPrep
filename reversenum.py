def reverseNum(num):
    rev =0
    while num>0:
        y = num %10
        rev = (rev*10)+y
        num = num//10
    print(rev)
num = int(input("enter the number to reverse: "))
reverseNum(num)
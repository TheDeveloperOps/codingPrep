def countDigit(num):
    count = 0
    while (num>0):
        count = count+1
        num= num//10
    return count
def powerOfNum(base,exponent):
    power = 1
    for i in range(1,exponent+1):
        power = power*base
    return power
def armstrongNumber(num):
    exponent = countDigit(num)
    sum =0
    while num > 0:
        base = num %10
        result = powerOfNum(base,exponent)
        sum = sum +result
        num = num//10
    return sum

num = int(input("enter the number : "))

if(num==armstrongNumber(num)):
    print("given number is armstrong")
else:
    print("not an armstrong")
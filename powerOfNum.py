def powerOfNum(base,exponent):
    power = 1
    for i in range(1,exponent+1):
        power = power*base
    print(power)
base = int(input("enter the base value: "))
exponent = int(input("enter the exponent value : "))
powerOfNum(base,exponent)
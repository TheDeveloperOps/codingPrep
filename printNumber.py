def prime(num):
    flag = True
    for i in range(2,num//2):
        if(num%i==0):
            flag =False
    return flag
num = int(input("enter "))
if(prime(num)==True):
    print("prime")
else:
    print("not a prime")
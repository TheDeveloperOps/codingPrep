def primeRange(lower,upper):
        for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num)
a = int(input("enter the inital value : "))
b = int(input("enter the end value: "))
primeRange(a,b)
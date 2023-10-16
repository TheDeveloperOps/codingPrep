def fibonacci(num):
    num1=0
    num2=1
    c=0
    if num<0:
        print("Enter a positive number ")
    elif num==2:
        print("fibo series ")
        print(num1)
        print(num2)
    else:
        print("Fibo series")
        while c<num:
            print(num1)
            nth= num1+num2
            num1 = num2
            num2 = nth
            c = c+1
nth_term = int(input("Enter the number: "))
fibonacci(nth_term)




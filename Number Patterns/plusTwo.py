def plusTwoPrint(n):
    p = 0
    for i in range(n):
        for j in range(i+1):
            print(p,end='')
        p+=2
        print()
plusTwoPrint(5)
def decNumber(n):
    p = n
    for i in range(n):
        for j in range(i,n):
            print(p,end=' ')
        p = p-1
        print()
decNumber(5)
def variableNumberColoumn(n):
    for i in range(n):
        p=1
        for j in range(i+1):
            print(p,end=' ')
            p=p+1
        print()
variableNumberColoumn(5)
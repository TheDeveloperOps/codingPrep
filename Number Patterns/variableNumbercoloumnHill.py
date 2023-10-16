def variableNumberColumnHill(n):
    for i in range(n):
        p=1
        for j in range(i,n):
            print(' ',end=' ')
        for j in range(i):
            print(p,end=' ')
            p+=1
        for j in range(i+1):
            print(p,end=' ')
            p+=1
        print() 
            
variableNumberColumnHill(5)
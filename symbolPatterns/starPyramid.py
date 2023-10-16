def pyramid(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
rows = int(input("enter the number of rows : "))
pyramid(rows)

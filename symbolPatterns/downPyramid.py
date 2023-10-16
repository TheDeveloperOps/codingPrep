def downPyramid(n):
    for i in range(n): 
        for j in range(i, n): 
            print('*', end=' ')
        print()
downPyramid(5)
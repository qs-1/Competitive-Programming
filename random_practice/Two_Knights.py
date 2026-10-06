n = int(input())
for k in range(1,n+1):
    cells = k*k

    print( (((cells**2)-cells)//2) - (((k-2)*(k-1)*2)*2) )
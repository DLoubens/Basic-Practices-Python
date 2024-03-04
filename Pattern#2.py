n=5
m=n//2+1

for x in range(1,n+1):
    for y in range(1,n+1):
        if (x == 1 or x == n or x == m or 
           (y == 1 and x > m) or 
           (y == n and x < m)):
            print("* " , end="")
        else :
            print("  " , end ="")
    print()
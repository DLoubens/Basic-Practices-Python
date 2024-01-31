n=5
m=n//2+1

for x in range(1,n+1):
    for y in range(1,n+1):
        if y==m or x==n or (x+y==m and y<=m):
            print("* " , end="")
        else :
            print("  " , end ="")
    print()
n=6
k=1

for x in range(1,n):
    for y in range(1,n):
        print("{:5}".format(k), end="")
        k += 1
    print()
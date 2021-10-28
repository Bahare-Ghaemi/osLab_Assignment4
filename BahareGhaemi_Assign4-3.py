m = int(input("enter m : "))
n = int(input("enter n : "))
mList = list(range(1,m+1))
nList = list(range(1,n+1))
for i in mList:
    for j in nList:
        print(i*j,end=" ")
    print()
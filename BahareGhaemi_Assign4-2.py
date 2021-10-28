m = int(input("enter m : "))
n = int(input("enter n : "))

mArr = list(range(1,m+1))
nArr = list(range(1,n+1))

for i in mArr:
    for j in nArr:
        if i % 2 == 0 and j % 2 == 0  or i % 2 != 0 and j % 2 != 0:
            print("#",end=" ")
        else:
            print("*",end=" ")
    print()
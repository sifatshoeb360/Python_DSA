
n = int(input())
n2 = n
for i in range(1,n+1):
    for j in range(i):
        print("*",end=' ')
    for j in range((n*2)-(i)*2):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=' ')

    print()
# print("uper done")
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=' ')
    for j in range((n*2)-(i*2)):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=' ')

    print()

    
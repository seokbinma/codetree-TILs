#별의 개수 2n-1
#공백의 개수 n-1
n= int(input())

for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
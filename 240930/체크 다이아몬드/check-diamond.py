#공백 n-1,n-2,..n-n//n-(n-1)...n-1 별 개수 1,2..n//n-1,...1
n= int(input())

for i in range(n):
    for j in range(n-1-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print()
for i in range(1,n):
    for k in range(n-(n-i)):
        print(" ",end="")
    for j in range(n-i):
        print("*",end=" ")
    print()
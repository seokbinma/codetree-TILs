n= int(input())

for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end=" ")
    for k in range(2*(n+1-i)-1):
        print("*",end=" ")
    print()
for a in range(2,n+1):
    for b in range(n-a):
        print(" ",end=" ")
    for c in range(2*(a)-1):
        print("*",end=" ")
    print()
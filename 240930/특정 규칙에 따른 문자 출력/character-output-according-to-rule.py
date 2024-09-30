#빈칸2,1,0 //1,2 특수기호 1,2,3// 2,1
n= int(input())
for i in range(n):
    for j in range(n-1-i):
        print(" ",end=" ")
    for k in range(i+1):
        print("@",end=" ")
    print()
for i in range(1,n):
    for j in range(n-i):
        print("@",end=" ")
    for k in range(i):
        print(" ",end=" ")
    print()
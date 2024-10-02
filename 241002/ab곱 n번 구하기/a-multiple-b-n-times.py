n=int(input())
for i in range(n):
    c=input().split()
    a,b=int(c[0]),int(c[1])
    d=1
    for i in range(a,b+1):
        d=d*i
    print(d)
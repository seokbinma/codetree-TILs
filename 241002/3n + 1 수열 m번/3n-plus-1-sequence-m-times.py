m=int(input())
for i in range(m):
    n= int(input())
    cnt=0
    while n!=1:
        if n%2==1:
            n=n*3+1
            cnt+=1
        else:
            n=n//2
            cnt+=1
    print(cnt)
n=int(input())
cnt=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if j>=i:
            if cnt>9:
                cnt=1
            print(cnt,end=" ")
            cnt+=1
        else:
            print(" ",end=" ")
    print()
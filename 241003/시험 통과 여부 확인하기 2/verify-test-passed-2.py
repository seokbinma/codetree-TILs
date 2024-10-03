n=int(input())
cnt=0
for i in range(n):
    st=list(map(int,input().split()))
    if (sum(st)//4) >=60:
        print("pass")
        cnt+=1
    else:
        print("fail")
print(cnt)
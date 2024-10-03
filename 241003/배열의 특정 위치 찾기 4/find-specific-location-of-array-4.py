arr=list(map(int,input().split()))
s=0
cnt=0
for i in arr:
    if i ==0:
        break
    else:
        if i%2==0:
            s+=i 
            cnt+=1
print(f"{cnt} {s}")
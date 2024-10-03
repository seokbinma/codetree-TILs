arr= list(map(int,input().split()))
a=[]
for i in arr:
    if i==0:
        break
    else:
        a.append(i)

for j in reversed(a):
    print(j,end=" ")
n=int(input())
a=[]
a.append(n)
cnt=0
b=2
c=1
while cnt!=2:
    c=n*b
    a.append(c)
    b+=1
    if c%5==0:
        cnt+=1
for i in a:
    print(i,end=" ")
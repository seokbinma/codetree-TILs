num=input().split()
a,b=int(num[0]),int(num[1])
c=0
for i in range(a,b+1):
    if 1920%i ==0 and 2880%i ==0:
        c=1

print(c)
n = input().split()
a,b,c= int(n[0]),int(n[1 ]),int(n[2])
d='NO'

for i in range (a,b+1):
    if c%i==0:
        d="YES"

print(d)
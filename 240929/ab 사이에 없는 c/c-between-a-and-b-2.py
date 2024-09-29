n = input().split()
a,b,c= int(n[0]),int(n[1 ]),int(n[2])
d='YES'

for i in range (a,b+1):
    if i%c==0:
        d="NO"

print(d)
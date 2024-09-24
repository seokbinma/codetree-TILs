num = input().split()
a,b,c = int(num[0]),int(num[1]),int(num[2])

if (a>b and a<c) or (a<b and a>c):
    print(a)
elif (b>a and b<c) or (c<b and b<a):
    print(b)
elif (c>b and c<a) or (a<c and c<b):
    print(c)
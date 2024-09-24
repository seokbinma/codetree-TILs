num = input().split()
a,b,c = int(num[0]),int(num[1]),int(num[2])

if (a>b and a<c) or (a<c and a>b):
    
    print(a)
elif (b>a and b<c) or (b<c and b>a):
    print(b)
else:
    print(c)
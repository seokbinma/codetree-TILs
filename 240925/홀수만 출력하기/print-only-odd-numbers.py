t= int(input())
a=[]
for i in range(t):
    b= int(input())
    if b%2==1 and b%3==0:
        a.append(b)
for i in a:
    print(i)
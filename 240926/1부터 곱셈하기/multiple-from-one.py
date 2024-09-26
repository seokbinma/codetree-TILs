n= int(input())

p=1
for i in  range(1,n+1):
    p*=i
    if p >=n:
        print(i)
        break
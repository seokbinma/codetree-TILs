n = input().split()
a= int(n[0])
b= int(n[1])
s=0
for i in range(a,b+1):
    if i%2 ==0:
        s+= i

print(s)
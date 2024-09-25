fc=0
tc=0
for i in range(10):
    n=int(input())
    if n%3==0:
        tc+=1
    if n%5==0:
        fc +=1

print(tc,fc)
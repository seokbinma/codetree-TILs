n=int(input())
a=[1]
a.append(n)
el=0
i=2
while True:
    el=a[i-2]+a[i-1]
    a.append(el)
    if el >100:
        break
    else:
        i+=1

for i in a:
    print(i,end=" ")
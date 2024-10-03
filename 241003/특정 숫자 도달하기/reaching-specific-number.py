i =0
a=[]
arr = list(map(int, input().split()))
for b in arr:
    if b>=250:
        break
    else:
        a.append(b)
        i+=1
sum=0
l=len(a)
for d in a:
    sum+= d
print(f"{sum} {sum/l:.1f}")
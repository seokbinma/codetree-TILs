arr=list(map(int,input().split()))
suma=0

for i in arr:
    if i ==0:
        break
    else:
        suma +=i
print(suma)
arr=list(map(int,input().split()))
suma=0

for i in arr:
    if i ==0:
        break
    else:
        suma +=1
print(arr[suma-1]+arr[suma-2]+arr[suma-3])
arr= list(map(int,input().split()))
el=0
for i in range(2,10):
    el=arr[i-1]+2*arr[i-2]
    arr.append(el)
for i in arr:
    print(i,end=" ")
arr = list(map(int, input().split()))
l=len(arr)
for i in range(l):
    if arr[i]%3==0:
        print(arr[i-1])
        break
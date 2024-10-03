arr= list(map(int,input().split()))
print(arr[0],arr[1],end=" ")
for i in range(2,10):
    temp = (arr[i-2]+arr[i-1]) %10
    print(temp,end=" ")
    arr.append(temp)
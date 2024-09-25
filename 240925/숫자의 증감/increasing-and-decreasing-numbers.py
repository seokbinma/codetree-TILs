arr = input().split()
a= arr[0]
n = int(arr[1])

if a=="A":
    i=1
    for i in range(1,n+1):
        print(i,end=" ")
else:
    i=0
    for i in range(n,0,-1):
        print(i,end=" ")
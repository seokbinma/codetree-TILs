arr= list(map(int,input().split()))
l=len(arr)
a=0
b=[]
for i in range(l):
    if arr[i]==0:
        a=i
        pass
    else:
        b.append(arr[i])


for i in b:
    if i%2 ==0:
        print(i//2,end=" ")
    else:
        print(i+3,end=" ")
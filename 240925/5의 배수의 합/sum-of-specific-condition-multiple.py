arr= input().split()
sum=0
a=int(arr[0])
b=int(arr[1])
temp=0
if a>b:
    temp=a
    a=b
    b=temp

for i in range(a,b +1):
    if i%5==0:
        sum+=i
print(sum)
arr = input().split()

a = int(arr[0])
b= int(arr[1])

sum=0
for i in range(a,b+1):
    sum+=i
print(sum)
arr = input().split()
a= int(arr[0])
b= int(arr[1])
if a>=b:
    c= a-b
    for i in range(c+1):
        print(a,end=" ")
        a-=1
else:
    c= b-a
    for i in range(c+1):
        print(b,end=" ")
        b-=1
num =input().split()
a,b,c=int(num[0]),int(num[1]),int(num[2])
condition = "N"
for i in range(a,b+1):
    if i % c ==0:
        condition="Y"
        break

if condition == "Y":
    print("YES")
else:
    print("NO")
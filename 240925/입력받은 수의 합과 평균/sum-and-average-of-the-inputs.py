n = int(input())
sum=0
for i in range(n):
    a= int(input())
    sum+=a
avg=sum/n
print(f"{sum} {avg:.1f}")
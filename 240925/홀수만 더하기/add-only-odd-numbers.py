n= int(input())
sum=0

for i in range(n):
    s=int(input())
    if s%2==1 and s%3==0:
        sum+=s

print(sum)
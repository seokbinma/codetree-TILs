sum=0
cnt=0
while True:
    a= int(input())
    if a//10 == 2 :
        sum+=a
        cnt+=1
    else:
        break
avg = sum/cnt
print(f"{avg:.2f}")
arr=list(map(int,input().split()))
cnt=0

for i in arr:
    if i ==0:
        break
    else:
        cnt+=1
#if 3 th error -> cnt =2 
suym=0
for i in range(cnt):
    suym+=arr[i]

avg=suym/cnt
print(f"{suym} {avg:.1f}")
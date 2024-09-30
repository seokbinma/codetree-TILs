n= int(input())
#3->2->1 홀 , 1-2-3 짝
cnt1,cnt2=1,n
for i in range(1,2*(n+1)-1):
    if i%2==1:
        for j in range(cnt1):
            print("*",end=" ")
        cnt1+=1
    elif i%2==0:
        
        for k in range(cnt2):
            print("*",end=" ")
        cnt2-=1
    print()
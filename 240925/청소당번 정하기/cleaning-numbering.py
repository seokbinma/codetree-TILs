n= int(input())
 
cls=0
fl=0
bt=0
for i in range(1,n+1):
    if i%2==0:
        if i%3==0:
            if i%12==0:
                bt+=1
            else:
                fl+=1
        else:
            cls+=1
        
    elif i%3==0:
        if i%12==0:
            bt+=1
        else:
            fl+=1
    elif i%12==0:
        bt+=1

print(cls,fl,bt)
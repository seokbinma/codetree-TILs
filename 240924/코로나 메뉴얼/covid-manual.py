H1 = input().split()
H2 = input().split()
H3 = input().split()

f1,T1 = H1[0],int(H1[1])
f2,T2 = H2[0],int(H2[1])
f3,T3 = H3[0],int(H3[1])

count = 0
if f1== 'Y':
    if T1 >= 37:
        count=count+1
if f2 =='Y':
    if T2 >= 37:
        count = count+1
if f3 =='Y':
    
    if T3 >=37:
        count = count +1

if count >=2:
    print("E")
else:
    print("N")
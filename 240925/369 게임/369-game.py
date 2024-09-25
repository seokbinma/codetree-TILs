n = input()
num= int(n)

for i in range(1,num+1):
    sn=str(i)
    if '3'in sn:
        print(0,end=" ")
    elif '6'in sn:
        print(0,end=" ")
    elif '9' in sn:
        print(0,end=" ")
    elif i%3 == 0:
        print(0,end=" ")
    else:
        print(i,end=" ")
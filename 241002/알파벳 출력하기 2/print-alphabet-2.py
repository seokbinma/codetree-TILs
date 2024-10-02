n=int(input())
a='A'
for i in range(n):
    for j in range(n):
        if ord(a)>ord('Z'):
            a='A' 
        if j>=i:
            print(a,end=" ")
            a=chr(ord(a)+1)
        else:
            print(" ",end=" ")
    
    print()
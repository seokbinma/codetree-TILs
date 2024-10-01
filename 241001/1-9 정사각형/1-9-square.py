n=int(input())

cn=1
for i in range(n):
    for j in range(n):
        if cn>=10:
            cn=cn%10+1
        print(cn,end="")
        cn+=1
    print()
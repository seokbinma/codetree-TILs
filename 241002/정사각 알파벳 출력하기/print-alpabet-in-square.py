n=int(input())
a=65
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(a),end="")
        a+=1
    print()
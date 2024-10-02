a=65
n=int(input())

for i in range(n):
    for j in range(n):
        if chr(a)=="Z":
            a=65
        if j<=i:
            print(chr(a),end="")
            a+=1
        
    print()
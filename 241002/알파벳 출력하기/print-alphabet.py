a=65
n=int(input())

for i in range(n):
    for j in range(n):
        if j<=i:
            print(chr(a),end="")
            if chr(a)=="Z":
                a=64
            a+=1
        
    print()
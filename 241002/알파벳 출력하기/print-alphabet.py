a=65
n=int(input())

for i in range(n):
    for j in range(n):
        if j<=i:
            print(chr(a),end="")
        if chr(a)==ord("Z"):
            a=65
        else:
            a+=1
    print()
a=65
n=int(input())

for i in range(n):
    for j in range(n):
        if j<=i:
            print(chr(a),end="")
            a+=1
        if chr(a)==ord("Z"):
            a=65
    print()
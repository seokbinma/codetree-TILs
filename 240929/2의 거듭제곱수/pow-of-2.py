N= int(input())
x=0
while True:
    if N == 2**x:
        break
    x+=1
print(x)
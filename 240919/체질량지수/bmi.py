human = input().split()
h=int(human[0])
w=int(human[1])
b = (10000*w)//(h*h)
if b>25:
    print(b)
    print("Obesity")
else:
    print(b)
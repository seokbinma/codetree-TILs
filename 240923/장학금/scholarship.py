test = input().split()
m=int(test[0])
l=int(test[1])
if m>=90 and l>=95:
    print(100000)
elif m>=90 and l >=90:
    print(50000)
else:
    print(0)
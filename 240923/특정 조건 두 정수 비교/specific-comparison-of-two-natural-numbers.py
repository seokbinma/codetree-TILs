num = input().split()
a= int(num[0])
b= int(num[1])


#대수 비교
if a > b:
    print(0, end=" ")
else:
    print(1, end=" ")
#동일비교
if a==b:
    print(1)
else:
    print(0)
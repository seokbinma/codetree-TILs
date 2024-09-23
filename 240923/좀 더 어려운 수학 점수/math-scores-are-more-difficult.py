s1 = input().split()
A= int(s1[0])
A1=int(s1[1])

s2 = input().split()
B= int(s2[0])
B1=int(s2[1])


if A>B:
    print("A")
elif A<B:
    print("B")
elif A==B:
    if A1>B1:
        print("A")
    else:
        print("B")
n = int(input())

if (n%2==0 and n%5==0) or (n%3==0 and n%2 ==1):
    print("true")
else:
    print("false")
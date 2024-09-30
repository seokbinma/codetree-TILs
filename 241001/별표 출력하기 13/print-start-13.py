n= int(input())

for i in range(1,2*n+1):
    if i%2==1:
        #1,3,5....2n-1 번쨰에서 n,n-1,n-2 출력하기
        for j in range(n-i//2):
            print("*",end=" ")
    else:
        #2,4,6,.... 에서 1,2,3...n
        for k in range(i//2):
            print("*",end=" ")

    print()
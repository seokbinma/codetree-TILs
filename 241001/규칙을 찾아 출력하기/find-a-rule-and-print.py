n=int(input())
#처음 끝 행 채우고 끝 열일 경우 다 채우기 나머지는 채워넣기
for i in range(n):
    for j in range(n):
        if i==0 or i==(n-1)or j==(n-1):
            print("*",end=" ")
        elif j<i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# 사용자로부터 입력받은 값을 공백으로 분리하여 리스트로 저장
arr = input().split()

# 각 요소를 정수로 변환
num1 = int(arr[0])
num2 = int(arr[1])

# 두 숫자의 곱 계산
c = num1 * num2

# 결과 출력
print(c)
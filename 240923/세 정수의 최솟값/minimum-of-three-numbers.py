nums = input().split()
a= int(nums[0])
b= int(nums[1])
c =int(nums[2])

if a<=b and a<=c:
    print(a)
elif b<=a and b<=c:
    print(b)
else:
    print(c)
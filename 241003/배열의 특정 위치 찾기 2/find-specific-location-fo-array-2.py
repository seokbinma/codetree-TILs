arr = list(map(int, input().split()))
fil_arr1= arr[::2]
fil_arr2= arr[1::2]
sum1=sum(fil_arr1)
sum2=sum(fil_arr2)
if sum1>sum2:
    print(sum1-sum2)
else:
    print(sum2-sum1)
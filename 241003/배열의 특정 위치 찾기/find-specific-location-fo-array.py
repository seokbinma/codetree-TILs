arr = list(map(int, input().split()))

fil_arr=arr[1::2]
fil_arr2=arr[2::3]
sum_ev=sum(fil_arr)
sum_ev2=sum(fil_arr2)
avg=sum_ev2/len(fil_arr2)
print(f"{sum_ev} {avg:.1f}")
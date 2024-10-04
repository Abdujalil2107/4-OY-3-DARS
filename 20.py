arr = [0, 1]

for i in range(2, 50):
    nums = arr[i - 1] + arr[i - 2]
    arr.append(nums)
print(arr)
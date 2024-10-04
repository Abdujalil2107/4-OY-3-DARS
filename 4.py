n = int(input("N... "))

arr = [1,2,3,4,5,6,7,8,9]

for i in range(len(arr)):
    for j in range(i,len(arr)):
        if n == (arr[i] + arr[j]):
            print(f"index = {i} index = {j} ")
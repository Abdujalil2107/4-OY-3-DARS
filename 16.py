arr_1 = [1, 2, 3]
arr_2 = [4, 5, 6]
arr_3 = [7, 8, 9]
arr_0 = [arr_1, arr_2, arr_3]
test = 0
max_arr = []

for i in arr_0:
    s = sum(i)
    if s > test:
        test = s 
        max_arr = i

print(max_arr)
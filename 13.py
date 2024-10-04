arr = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d')]
test = []

for i in range(len(arr)):
    a = arr[i] 
    if a != (): 
        test.append(a)
print(test)
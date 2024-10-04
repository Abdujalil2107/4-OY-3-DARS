n = int(input("n... "))
i = n
tub = 0
test = 0
arr = []

while(True):
    i+=1
    for j in range(1,i+1):
        if i%j==0:
            test+=1
    if test==2:
        tub+=1
        arr.append(i)
        print(i)
    test = 0
    if tub == 5:
        break
print(arr)
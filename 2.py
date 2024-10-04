a = int(input("A... "))
b = int(input("B... "))

arr = []

if a>b:
    a,b = b,a

for i in range(b,a-1,-1):
    if i%2==1:
        arr.append(i)
print(arr)
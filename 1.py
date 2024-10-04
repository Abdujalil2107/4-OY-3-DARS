a = int(input("A... "))
b = int(input("B... "))

arr = []

if a>b:
    a,b = b,a

for i in range(a,b+1):
    arr.append(i)
print(arr)
arr = ["olim", "karim", "ali", "salimboi", "alkhan", "sherbek", "tursunkhon"]

ism = list(map(str.lower, input("ism kiriting... ").split()))

while True :
    if ism in arr:
        print(f"{ism} bu ism bor edi")
        break
    else:
        arr.append(ism)
        print(f"{ism} ism qo'shildi !!!")
        break

print(" ro'yxat... ", arr)
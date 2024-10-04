a = [('item1', '15.10'), ('item2', '12.20'), ('item3', '24.5')]
b= []
for i in a:
    b.append(float(i[1]))
b.sort()

listta =[]
for i in b:
    for j in a:
        if i== float(j[1]):
            listta.append(j)
print(listta)
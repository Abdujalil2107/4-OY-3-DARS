arr = [1,2,3,4,5,6,"123456","salom",True]
txt = []
other = []

for i in arr:
    if type(i) == str:  
        txt.append(i)
    else:
        other.append(i)

txt.sort()
other.sort(reverse=True)

print(txt)
print(other)
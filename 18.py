nums=(1,2,45,6,3,2,4,6,2,6,7,8,3,21,12,3)
juft=[]
toq=[]

for i in range(len(nums)):
    if i%2==0:
        juft.append(nums[i])
    else:
        toq.append(nums[i])
print(toq)
print(juft)
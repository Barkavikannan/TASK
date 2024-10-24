array=[1,2,3,4,5]
sum=0
result=[]
for i in range(len(array)):
    sum=sum+array[i]
    result.append(sum)
print(result)
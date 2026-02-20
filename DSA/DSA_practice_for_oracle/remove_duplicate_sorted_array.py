a=[1,1,2,2,2,3,3,3,3,4,5,6,6,7,8,8,8,9,9]

j=0

for i in range(1,len(a)):
    if a[i]!=a[j]:
        j+=1
        a[j]=a[i]

print(a[:j+1])


a=[1,1,1,2,2,3,3,4,5,6,6,7,8,9,9,9]


"""
hash_dict={}


count=0
for i in range(0,len(a)):
    if a[i] in hash_dict:
        continue
    else:
        hash_dict[a[i]]=1
        count+=1

print(count)

print(a)


j=0
for key,value in hash_dict.items():
    print(key,value)
    a[j]=key
    j=j+1

print(a)
"""


# find some optimal solution

i=0
j=i+1

while j <len(a):
    if a[i]!=a[j]:
        i=i+1
        a[i],a[j]=a[j],a[i]
        j=j+1
    else:
        j=j+1

print(a)
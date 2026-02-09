# inmplement selection sort 

a=[1,3,2,5,4,6,4,3,7,8,4,2]

for i in range(0,len(a)):
    key=a[i]
    j=i-1

    while j>=0 and a[j]>key:
        a[j+1]=a[j]
        j=j-1

    a[j+1]=key

print(a)


# insertion sort for desending order

b=[1,3,2,5,4,6,4,3,7,8,4,2]

for i in range(0,len(b)):
    key=b[i]
    j=i-1

    while j>=0 and b[j]>key:
        b[j+1]=b[j]
        j=j-1

    b[j+1]=key

print(b)
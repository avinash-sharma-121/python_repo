# Implement bubble sort in python in Assending order

a=[1,3,2,5,4,6,4,3,7,8,4,2]

print("input for sorting in Assenidng order")
print(a)

def bubble_sort_assending(a):
    for i in range(0,len(a)):
        for j in range(0,len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

    print("Output:- ")
    print(a)
bubble_sort_assending(a)

# Implement bubble sort in python in Dessending order

b=[1,3,2,5,4,6,4,3,7,8,4,2]

print("input for sorting in Desending order")
print(b)

for i in range(0,len(b)):
    for j in range(0,len(b)-1):
        if b[j] < b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]

print("Output:- ")
print(b)



# optimieze way implement bubble sort

c=[1,3,2,5,4,6,4,3,7,8,4,2,123]
d=[1,2,3,4,5,6,7,8,9,10,11,12]

print("input for sorting (more optimieze way) in Desending order")
print(c)

def bubble_sort_optmizse(a):
    for i in range(0,len(a)):
        is_swapped=False
        for j in range(0,len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                is_swapped=True

        #print(is_swapped)
        if is_swapped==False:
            break

    print("Output:- ")
    print(a)

bubble_sort_optmizse(c)

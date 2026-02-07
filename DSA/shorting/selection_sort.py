# Implement selection sort in python in Assending order

a=[1,3,2,5,4,6,4,3,7,8,4,2]

print("input for sorting in Assenidng order")
print(a)

def select_sort_assending(a):

    for i in range(0,len(a)):
        min_index=i
        for j in range(i+1,len(a)):
            if a[min_index]>a[j]:
                min_index=j
        
        a[min_index],a[i]=a[i],a[min_index]
        #temp=a[i]
        #a[i]=a[min_index]
        #a[min_index]=temp
        #print(a) 

    print(a)

print("output:- ")
select_sort_assending(a)

# Implement selection sort in python in Desending Order


b=[1,3,2,5,4,6,4,3,7,8,4,2]
print("input for sorting in Desending order")
print(b)
def insertion_sort_desending(b):
    for i in range(0,len(b)):
        max_index=i
        for j in range(i+1,len(b)):
            if b[max_index]<b[j]:
                max_index=j

        b[max_index],b[i]=b[i],b[max_index]

    print(b)

print("Output:- ")
insertion_sort_desending(b)
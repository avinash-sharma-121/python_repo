#bubble sort

a=[1,3,6,2,9,6,7,1,5]

for i in range(0,len(a)):
    for j in range(0,len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

#print(a)

#selection sort

a=[1,3,6,2,9,6,7,1,5]

#print(a)

for i in range (0,len(a)):
    min_ind=i
    for j in range(i,len(a)):
        if a[min_ind]>a[j]:
            min_ind=j

    a[i],a[min_ind]=a[min_ind],a[i]

#print(a)


# implement merge sort

#a=[1,2,5,8,33,78]
#b=[3,4,8,9,23]


def merger_two_array(left_arr,right_arr):
    res=[]
    len_left_arr=len(left_arr)
    len_right_arr=len(right_arr)
    i=j=0
    while i < len_left_arr and j <len_right_arr:
        if left_arr[i] > right_arr[j]:
            res.append(right_arr[j])
            j+=1
        else:
            res.append(left_arr[i])  
            i+=1
    
    if i < len_left_arr:
        while i < len_left_arr:
            res.append(left_arr[i])
            i+=1
    if j < len_right_arr:
        while j < len_right_arr:
            res.append(right_arr[j])
            j+=1

    return res

#print(merger_two_array(a,b))


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid=len(arr)//2

    left_arr=merge_sort(arr[:mid])
    right_arr=merge_sort(arr[mid:])

    return merger_two_array(left_arr,right_arr)

a=[1,3,6,2,9,6,7,1,5]
#print(merge_sort(a))
    

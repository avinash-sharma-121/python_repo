a=[1,3,2,5,4,6,4,3,7,8,4,2]

def partition_fun(arr,low,high):
    pivot=arr[low]
    i=low
    j=high

    while i<j:
        while arr[i]<=pivot and i <= high-1:
            i+=1
        while arr[j]>pivot and j >=low+1:
            j-=1

        if i<j:
            arr[i],arr[j]=arr[j],arr[i]

    arr[low],arr[j]=arr[j],arr[low]

    return j 


def quick_sort(arr,low,high):
    if low<high:
        pivot_ind=partition_fun(arr,low,high)
        quick_sort(arr,low,pivot_ind - 1)
        quick_sort(arr,pivot_ind + 1,high)

quick_sort(a,0,len(a)-1)

print(a)
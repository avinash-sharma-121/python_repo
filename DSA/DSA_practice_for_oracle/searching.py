# learning search

a=[1,2,3,4,5,6,8,10]

n=12

def search(n):
    for i in range(0,len(a)):

        if a[i]==n:
            return True

    return False

print(search(6))


## binary search

def binary_search(n):

    l=0
    r=len(a)-1

    while l<=r:

        mid= (l + r)//2
        if a[mid]==n:
            return True
        elif a[mid]<n:
            l=mid+1
        else:
            r=mid-1

    return False

print(binary_search(6))


a=[1,1,4,4,5,5,6,6,6,8,12]
b=[1,2,2,3,3,4,4,5,7,8,9]

def merge_two_sorted_array_without_duplicate(a,b):
    ans=[]
    if a[0] <= b[0]:
        ans.append(a[0])
    else:
        ans.append(b[0])
    i=j=1
    while i<len(a) and j < len(b):
        if a[i]<=b[j]:
            if a[i] != ans[-1]:
                ans.append(a[i])
            i+=1
        else:
            if b[j] != ans[-1]:
                ans.append(b[j])
            j+=1
    
    if i < len(a):
        while i < len(a):
            if ans[-1] != a[i]:
                ans.append(a[i])
            i+=1

    if j < len(b):
        while j < len(b):
            if ans[-1] != b[j]:
                ans.append(b[j])
            j+=1

    return ans

print(merge_two_sorted_array_without_duplicate(a,b))
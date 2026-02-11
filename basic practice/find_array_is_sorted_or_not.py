a=[12,-23,10,34,54,11,4,5,89,31,21]

b=[1,2,3,4,5,56,6,67]


def check_list_soted_or_not(a):
    for i in range(0,len(a)-1):
        if a[i] <= a[i+1]:
            continue
        else:
            return False
        
    return True

print(check_list_soted_or_not(a))
print(check_list_soted_or_not(b))
    
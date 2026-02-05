a=[1,2,3,4,5,6,7,8,9,10]

def reverse_list(a):
    a=a[::-1]
    return a

print(reverse_list(a))

b=[1,2,3,4,5,6,7,8,9,10]

def manual_reverse_list(b):
    reverse_list=[]
    for i in b:
        reverse_list.insert(0,i)
    return reverse_list

print(manual_reverse_list(b))
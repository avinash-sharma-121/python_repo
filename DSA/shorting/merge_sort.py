

a=[1,3,2,5,4,6,4,3,7,8,4,2]

def merge_two_array(left,right):
    len_left=len(left)
    len_right=len(right)
    i=j=0
    output=[]
    while i< len_left and j<len_right:
        if left[i] <= right[j]:
            output.append(left[i])
            i+=1
        else:
            output.append(right[j])
            j+=1
        
    if i < len_left:
        while i<len_left:
            output.append(left[i])
            i+=1
    if j < len_right:
        while j < len_right:
            output.append(right[j])
            j+=1
    return output

c=[1,2,5,8,33,78]
b=[3,4,8,9]

#print(merge_two_array(b,c))

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    left=merge_sort(left_arr)
    right=merge_sort(right_arr)
    return merge_two_array(left,right)

print(f"Before soritng:-  {a}")
print(f"After merge sorting:- {merge_sort(a)}")


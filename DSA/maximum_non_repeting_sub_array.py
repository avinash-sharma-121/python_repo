#Input:  "abcabcdbb"
#Output: 3
#Explanation: "abc"

a="abcabcdbb"

hash_list=set()
max_len=0
left=0
start=0

for right in range(len(a)):
    while a[right] in hash_list:
        hash_list.remove(a[left])
        left=left+1
        
    hash_list.add(a[right])

    if max_len < right-left+1:
        max_len=right-left+1
        start=left

   

print(max_len)
print(a[start:start+max_len])


#🔥 Return Actual Substring (Interview Gold)


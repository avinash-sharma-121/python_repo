a=[1,2,6,4,3,9,8,5]

#Brute force mathod
target=18
def two_sum(target):
    for i in range(len(a)):
        for j in range(i,len(a)):
            if i==j:
                continue
            if a[i]+a[j]==target:
                print("Brute force Yes")
                print(f"Indeces: {i,j}")
                return
    
    print("No")

two_sum(target)

# better solution with hash_map

def two_sum_hash_map(target):
    hash_map={}
    for i in range(len(a)):
        find_no=target-a[i]
        if find_no in hash_map:
            print("YES")
            get_second_ind=hash_map.get(find_no,0)
            print(f"Index: {i,get_second_ind}")
            return
        
        else:
            hash_map[a[i]]=i

    print("NO")

two_sum_hash_map(target)


#Two sum problem with sorted array

a=[1,2,3,4,5,8,9]

print("two sum with sorted Array")
l=0
r=len(a)-1

while l<r:
    #print(a[l],a[r])
    if a[l]+a[r]==target:
        print("True")
        print(f"Index {l,r}")
        break
    elif a[l]+a[r] > target:
        r-=1
    else:
        l+=1
    
#Input:  [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: [4,-1,2,1] → sum = 6


a=[-2,1,-3,4,-1,2,1,-5,4]

# apply brute force

max_sum=float("-inf")

for i in range(0,len(a)):
    current_sum=0
    for j in range(i,len(a)):
        current_sum=current_sum+a[j]

        #print(current_sum)
        max_sum=max(max_sum,current_sum)

print(max_sum)

## Using kadanace algo

max_sum=a[0]
current_sum=a[0]

for i in range(len(a)):
    current_sum=max(a[i],current_sum+a[i])
    max_sum=max(max_sum,current_sum)

print(max_sum)


## return the array with max sum also uisng brute force

l=r=0
max_sum=0


for i in range(len(a)):
    current_sum=0
    for j in range(i, len(a)):
        current_sum=current_sum+a[j]

        if max_sum < current_sum:
            max_sum=current_sum
            l=i
            r=j

print(i,j)
print(f"max_value: {max_sum}")
print(f"Sub Array {a[l:r+1]}")


## return the array and max_sum also uisng kadanc algo

max_sum=0
current_sum=0

l=r=temp_ind=0
for i in range(len(a)):
    if a[i] > a[i]+current_sum:
        temp_ind=i
        current_sum=a[i]
    else:
        current_sum+=a[i]

    if max_sum < current_sum:
        l=temp_ind
        r=i
        max_sum=current_sum

print(l,r)
print(f"max_value: {max_sum}")
print(f"Sub Array {a[l:r+1]}")


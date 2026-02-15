#basic Approach brute force

height=[4,2,0,3,2,5]

## brute force mathod

total_water=0
for i in range(len(height)):
    
    #find max_left
    max_left=0
    for j in range(0,i+1):
        max_left=max(max_left,height[j])
    
    #find max_right
    max_right=0
    for j in range(i, len(height)):
        max_right=max(max_right,height[j])
    
    water_at_index=min(max_left,max_right)- height[i]

    if water_at_index > 0:
        total_water+=water_at_index
print(total_water)



#now we will try left_max_array and right_max_array method
total_water=0

n=len(height)
left_max_array=[0]*n
right_max_array=[0]*n
left_max_array[0]=height[0]
right_max_array[n-1]=height[n-1]

for i in range(1,len(height)):
    max_left=max(left_max_array[i-1],height[i])
    left_max_array[i]=max_left

for i in range(n-2,-1,-1):
    max_right=max(right_max_array[i+1],height[i])
    right_max_array[i]=max_right

print(left_max_array)
print(right_max_array)

for i in range(0,n):
    total_water+=min(left_max_array[i],right_max_array[i])-height[i]

print(total_water)


#this time we will use two pointer method

total_water=0
lmax=0
rmax=0
l=0
r=n-1

while l<r:
    lmax=max(lmax,height[l])
    rmax=max(rmax,height[r])

    if lmax < rmax:
        total_water+=lmax-height[l]
        l+=1
    else:
        total_water+-rmax-height[r]
        r-=1
print(total_water)
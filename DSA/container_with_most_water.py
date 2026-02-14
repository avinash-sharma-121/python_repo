height = [1,8,6,2,5,4,8,3,7]

#leet code problem

# brute force approach

most_water=0
for i in range(len(height)):
    current_water=0
    for j in range(i+1,len(height)):
        width=j-i
        min_height=min(height[i],height[j])
        current_water=width*min_height

        most_water=max(most_water,current_water)
        
print(most_water)

# This time we will try with two pointer approach

most_water=0

left=0
right=len(height)-1

while left<right:
    width=right-left
    min_height=min(height[left],height[right])
    ans=width*min_height
    most_water=max(most_water,ans)

    if left < right:
        left+=1
    else:
        right-=1

print(most_water)
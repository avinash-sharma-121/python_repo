#[10, 5, 20, 8]

def second_largest_no(nums):
    max_no=float("-inf")
    second_max=float("-inf")

    for i in range(len(nums)):
        if max_no < nums[i]:
            second_max=max_no
            max_no=nums[i]
        
        elif second_max < nums[i] and max_no != nums[i]:
            second_max=nums[i]
    return second_max

print(second_largest_no([5,5,5]))

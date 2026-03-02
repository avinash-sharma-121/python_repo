class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        
        sum=0
        i=0
        for i in range(0,k):
            sum=sum+nums[i]
            print(sum)
        left=0
        max_sum=sum
        for right in range(k,len(nums)):
            sum=sum+nums[right]
            sum=sum-nums[right-k]
            max_sum=max(max_sum,sum)
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = nums[0]
        currSum = 0
        
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSum = max(maxSum, currSum)
            
        return maxSum
        
# Notes Learned:
# - Make sure to realize that the max sum doesn't need to include the negative number at beginning of sub array
# - If subArray goes to 0 it is not a good subarray.


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax=globalMax=nums[0]
        for i in range(1,len(nums)):
            currMax = max(nums[i],currMax+nums[i])
            if currMax > globalMax:
                globalMax = currMax
        return globalMax

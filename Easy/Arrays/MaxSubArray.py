class Solution:
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

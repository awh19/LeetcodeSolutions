class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = dict()
        for index, num in enumerate(nums):
            diff = target - num
            if diff not in numDict:
                numDict[num] = index
            else:
                return [numDict[diff],index]
                
    # Remember, you don't have to initialize the hashmap initially. If you check for the difference you can go over in one pass.
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            return self.intersect(nums2,nums1)
        
        freqDict = dict()
        ans = []
        
        
        for num in nums1:
            if num in freqDict:
                freqDict[num] = freqDict[num]+1
            else:
                freqDict[num] = 1
        
        for num in nums2:
            if num in freqDict and freqDict[num] > 0:
                freqDict[num] = freqDict[num]-1
                ans.append(num)
        
        return ans
    
    
    # What if the given array is already sorted? How would you optimize your algorithm?
        # When sorted you can use a simple two pointer iteration. Since both are ascending just check whether first array[i] is bigger than second array[j] and increment
    
    # What if nums1's size is small compared to nums2's size? Which algorithm is better?
    
    # What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
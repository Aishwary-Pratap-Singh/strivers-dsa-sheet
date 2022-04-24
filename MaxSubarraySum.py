#TC O(N)
# SC O(1)

import sys
INT_MIN = -sys.maxsize
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = 0
        currSum = 0
        biggest = INT_MIN
        
        for i in range(len(nums)):
            currSum += nums[i]
            
            maxSum = max(currSum,maxSum)
            if currSum < 0:
                currSum = 0
                
            if nums[i] > biggest:
                biggest = nums[i]
        
        if maxSum == 0:
            return biggest
        return maxSum
        

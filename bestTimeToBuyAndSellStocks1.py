# tc = o(n)

class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        mini = nums[0]
        profit = 0
        for i in range(len(nums)):
            if nums[i] < mini:
                mini = nums[i]
            
            profit = max(nums[i] - mini , profit)
        return profit
                
        

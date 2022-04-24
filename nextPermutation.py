class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        
        for i in range(n-2,-2,-1):
            if nums[i+1] > nums[i]:
                ind1 = i
                break
        
        if i < 0:
            i = 0
            j = n-1
            while i < j:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
            return nums
            
        
        for i in range(n-1,-1,-1):
            if nums[i] > nums[ind1]:
                ind2 = i 
                break
                
        nums[ind1],nums[ind2] = nums[ind2],nums[ind1]
        
        i = ind1+1
        j = n-1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
        
        return nums
        
                
        

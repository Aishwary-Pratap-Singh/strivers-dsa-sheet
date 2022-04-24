# Tc = O(n)
#sc = O(1)

class Solution:
    def swap(self,arr,i,j):
        arr[i],arr[j] = arr[j],arr[i]
        
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        low = 0 
        mid = 0
        high = len(nums)-1
        
        while mid <= high:
            if nums[mid] == 0:
                self.swap(nums,low,mid)
                low += 1
                mid += 1
                
            elif nums[mid] == 1:
                mid += 1
            # if nums[mid] == 2:
            else:
                self.swap(nums,mid,high)
                high -= 1
                # mid += 1
            
        return nums
        
        
        

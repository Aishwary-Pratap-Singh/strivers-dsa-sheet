
#  tc = nlogn
class Solution:
    
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n = len(nums1)
        m = len(nums2)
        for i in range(n-m,n):
            nums1[i] = nums2[i%m]
            
        nums1.sort()
        

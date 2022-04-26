# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# tc = O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = None
        
        while head != None:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return curr
        

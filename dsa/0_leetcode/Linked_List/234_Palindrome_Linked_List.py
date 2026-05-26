# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head 
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        # after this slow will pointing to the middle.
        # reverse the linked list at slow
        
        prev = None
        while slow:
            slow.next = prev
            prev = slow
            slow = slow.next
            
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
            
        
sol = Solution()
result = sol.isPalindrome(head, x)

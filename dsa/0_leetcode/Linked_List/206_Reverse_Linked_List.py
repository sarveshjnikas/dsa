class ListNode():
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
              
    def BuildLinkedList(arr):
        dummy = ListNode()
        curr = dummy
        for element in arr:
            curr.next = ListNode(element)
            curr = curr.next
        return dummy.next
        
class Solution:
    def reverseList(self, head):
        prior = None
        while head:
            temp = head.next
            head.next = prior
            head = temp
            prior = head
        return head

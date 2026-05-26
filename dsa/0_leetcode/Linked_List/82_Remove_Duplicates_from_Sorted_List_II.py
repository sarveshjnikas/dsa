# ---------- Helper functions ----------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        start = head
        last_dist = None
        while start and start.next:
            print(start.val)
            if start.next.val != start.val:
                last_dist = start
                start = start.next
            else:
                while start.next and start.val == start.next.val:
                    start = start.next
                start = start.next
                last_dist.next = start
        return head
    
head = build_linked_list([1,2])
sol = Solution()
result = sol.deleteDuplicates(head)

print(linked_list_to_list(result))

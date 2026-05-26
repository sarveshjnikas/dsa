class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0, head) # we use dummy so that if head is removed then also it works
        slow = dummy
        fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

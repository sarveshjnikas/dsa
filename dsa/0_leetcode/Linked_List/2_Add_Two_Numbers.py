from typing import List
from collections import Counter

class ListNode:
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            first_digit = l1.val if l1 else 0
            second_digit = l2.val if l2 else 0

            total = first_digit + second_digit + carry
            digit_to_append = total % 10
            carry = total // 10

            curr.next = ListNode(digit_to_append)
            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

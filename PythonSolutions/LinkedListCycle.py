# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        fast = slow = head
        while (True):
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            if not fast or not slow:
                return False
            if fast == slow:
                return True
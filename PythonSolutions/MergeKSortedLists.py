# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Use divide and concur on 2 lists
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = cursor = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    cursor.next = l1
                    l1 = l1.next
                else:
                    cursor.next = l2
                    l2 = l2.next
                cursor = cursor.next
            if (l1 == None) or (l2 == None):
                cursor.next = l1 or l2
            return dummy.next

        numLists = len(lists)

        if numLists < 1:
            return None
        interval = 1

        while interval < numLists:
            for i in range(0, numLists - interval, interval * 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val:int = val
        self.next:ListNode = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        prime = ListNode()
        current = prime
        l1 = list1
        l2 = list2
        while l1 is not None:
            while l2 is not None:
                if l2.val <= l1.val:
                    current.next = l2
                    current = current.next
                    l2 = l2.next
                else:
                    break
            current.next = l1
            current = current.next
            l1 = l1.next
            if l2 is None:
                break
        if l2 is not None:
            current.next = l2
        return prime.next



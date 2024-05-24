# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        remainder = 0
        cur_node = result
        while l1 != None or l2 != None or remainder > 0:
            l1_value = 0
            l2_value = 0
            if l1 != None:
                l1_value = l1.val
                l1 = l1.next
            if l2 != None:
                l2_value = l2.val
                l2 = l2.next
            sum = l1_value + l2_value + remainder
            cur_node.val = sum%10
            remainder = sum//10
            if l1 != None or l1 != None or remainder > 0:
                new_node = ListNode()
                cur_node.next = new_node
                cur_node = new_node
        return result
        

def create_list_of_listnodes(values):
    head = None
    prev = None
    for val in values:
        new_node = ListNode(val)
        if head is None:
            head = new_node  # Set the first node as head
        else:
            prev.next = new_node  # Link the previous node to the new one
        prev = new_node  # Update the previous node to the current one
    return head

# To instantiate the class and call the method
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution_instance = Solution()
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    solution_instance.addTwoNumbers(create_list_of_listnodes(l1), create_list_of_listnodes(l2))

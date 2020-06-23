"""
You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order and each of their nodes 
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the 
number 0 itself.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    sum = l1.val + l2.val

    carry = sum // 10
    digit = sum % 10

    # Return head of linked list, but add to tail
    l = ListNode(digit)
    curr = l

    while carry or l1.next or l2.next:
        sum = carry

        if l1.next:
            l1 = l1.next
            sum += l1.val

        if l2.next:
            l2 = l2.next
            sum += l2.val

        carry = sum // 10
        digit = sum % 10

        curr.next = ListNode(digit)
        curr = curr.next

    return l

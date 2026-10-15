# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = None
        temp = None
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            a = 0
            b = 0

            if l1 is not None:
                a = l1.val
                l1 = l1.next

            if l2 is not None:
                b = l2.val
                l2 = l2.next

            total = a + b + carry
            digit = total % 10
            carry = total // 10

            new_node = ListNode(digit)

            if head is None:
                head = new_node
                temp = new_node
            else:
                temp.next = new_node
                temp = new_node

        return head
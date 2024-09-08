"""Given the head of a linked list, remove the nth node from the end of the list and return its head."""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head

        # Move temp `n` steps forward
        for i in range(n):
            temp = temp.next


        if not temp:
            return head.next

        back = head
        while temp.next:
            temp = temp.next
            back = back.next


        back.next = back.next.next

        return head
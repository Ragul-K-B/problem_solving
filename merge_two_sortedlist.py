"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list."""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        temp = list1
        while temp:
            l.append(temp.val)
            temp = temp.next

        temp = list2
        while temp:
            l.append(temp.val)
            temp = temp.next
        l = sorted(l)
        print(l)
        if len(l) == 0:
            return list1
        node = ListNode(l[0], None)
        temp = node
        prev = node

        for i in range(1, len(l)):
            new_node = ListNode(l[i])
            while temp.next:
                temp = temp.next
            temp = new_node
            prev.next = temp
            prev = prev.next

        return node


"""Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity."""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if temp == None or temp.next == None:
            return head
        i = 1
        odd = []
        eve = []
        while temp:
            if i % 2 == 0:
                eve.append(temp)
            else:
                odd.append(temp)
            i += 1
            temp = temp.next

        head = odd[0]
        cur = head

        for i in range(1, len(odd)):
            print(cur.val)
            cur.next = odd[i]
            cur = cur.next

        for j in eve:
            print(cur.val)
            cur.next = j
            cur = cur.next
        cur.next = eve[-1]
        cur.next = None

        return head


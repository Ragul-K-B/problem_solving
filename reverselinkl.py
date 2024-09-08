# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        lis = []
        while temp:
            lis.append(temp.val)
            temp = temp.next
        lis = lis[::-1]
        newn = ListNode(0)
        ans = newn
        for i in lis:
            tempt = ListNode(i)
            ans.next = tempt
            ans = ans.next
        return newn.next

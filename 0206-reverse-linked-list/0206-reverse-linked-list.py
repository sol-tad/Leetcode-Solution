# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revNode=None
        curr=head
        while curr:
            nextNode=curr.next
            curr.next=revNode
            revNode=curr
            curr=nextNode
        return revNode
        


        
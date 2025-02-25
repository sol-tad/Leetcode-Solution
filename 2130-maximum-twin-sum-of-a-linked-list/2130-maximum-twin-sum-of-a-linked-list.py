# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            #reverse first half node
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        maxres=0

        while slow:
            maxres=max(maxres,prev.val+slow.val)
            prev=prev.next
            slow=slow.next
        return maxres
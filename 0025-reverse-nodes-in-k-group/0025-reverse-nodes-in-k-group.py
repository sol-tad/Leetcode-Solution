# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        groupPrev=dummy

        while True:
            kth=self.getkth(groupPrev,k)
            if not kth:
                break
            groupNext=kth.next

            #reverse the group
            prev=kth.next
            curr=groupPrev.next
            while curr!=groupNext:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            temp=groupPrev.next
            groupPrev.next=kth
            groupPrev=temp

        return dummy.next

    def getkth(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr
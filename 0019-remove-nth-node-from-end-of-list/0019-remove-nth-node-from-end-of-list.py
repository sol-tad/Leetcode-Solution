# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fptr=head
        bptr=head
        

        while n>0:
            fptr=fptr.next
            n-=1
        
        if not fptr:
            return head.next

        while fptr.next:
            fptr=fptr.next
            bptr=bptr.next
        print(bptr.val)
        print(fptr.val)
        bptr.next=bptr.next.next

        return head

        
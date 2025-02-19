class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.dummy=Node()   

    def get(self, index: int) -> int:
        head=self.dummy.next
        temp=head
        counter=0
        while temp and counter<index:
            temp=temp.next
            counter+=1
        if counter==index and temp:
            return temp.val
        
        return -1

    def addAtHead(self, val: int) -> None:
       newNode=Node(val)
       newNode.next=self.dummy.next
       self.dummy.next=newNode

    def addAtTail(self, val: int) -> None:
        newNode=Node(val)
        temp=self.dummy
        while temp and temp.next:
            temp=temp.next
        temp.next=newNode

    def addAtIndex(self, index: int, val: int) -> None:
        newNode=Node(val) 
        temp=self.dummy
        counter=0
        while temp and counter<index:
            temp=temp.next
            counter+=1
        if counter!=index:
            return
        if temp is None:
             return
        newNode.next=temp.next
        temp.next=newNode

    def deleteAtIndex(self, index: int) -> None:
        temp=self.dummy
        counter=0
        while temp and counter<index:
            temp=temp.next
            counter+=1
        if temp is None or temp.next is None:
            return
        
        temp.next=temp.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
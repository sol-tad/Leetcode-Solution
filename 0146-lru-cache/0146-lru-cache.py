class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hmcache={}

        self.lru=Node(0,0)
        self.mru=Node(0,0)

        self.lru.next=self.mru
        self.mru.prev=self.lru
        
    def remove(self,node):
        prevnode=node.prev
        nextnode=node.next
        prevnode.next=nextnode
        nextnode.prev=prevnode
    def insert(self,node):
        prevnode=self.mru.prev
        nextnode=self.mru
        prevnode.next=node
        nextnode.prev=node
        node.next=nextnode
        node.prev=prevnode

    def get(self, key: int) -> int:
        if key in self.hmcache:
            self.remove(self.hmcache[key])
            self.insert(self.hmcache[key])
            return self.hmcache[key].val
        return -1  

    def put(self, key: int, value: int) -> None:
        if key in self.hmcache:
            self.remove(self.hmcache[key])
        self.hmcache[key]=Node(key,value)
        self.insert(self.hmcache[key])
        if len(self.hmcache) > self.capacity:
            lruu=self.lru.next
            self.remove(lruu)
            del self.hmcache[lruu.key]


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
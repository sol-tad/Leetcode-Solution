class DataStream:

    def __init__(self, value: int, k: int):
        self.k=k
        self.val=value
        self.queue=deque()
        self.count=0

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num==self.val:
             self.count+=1
     

        if len(self.queue)>self.k:
            removed=self.queue.popleft()
            if removed==self.val:
             self.count-=1
        elif len(self.queue)< self.k:
            return False

        if self.count==self.k:
            return True
        else:
            return False

        


    


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
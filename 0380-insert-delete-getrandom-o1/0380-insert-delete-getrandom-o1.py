class RandomizedSet:

    def __init__(self):
        self.hm={}

    def insert(self, val: int) -> bool:
        if val in self.hm:
            return False
        else:
            self.hm[val]=1
            return True

    def remove(self, val: int) -> bool:
        if val in self.hm:
            self.hm.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return int(random.choice(list(self.hm.keys())))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
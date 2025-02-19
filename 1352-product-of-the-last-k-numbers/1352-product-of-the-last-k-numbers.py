class ProductOfNumbers:

    def __init__(self):
        self.prefixProduct=defaultdict(int)
        self.currProduct=1
        self.index=0

    def add(self, num: int) -> None:
        self.currProduct*=num
        if num==0:
            self.prefixProduct.clear()
            self.currProduct=1
            self.index=0
        else:
            self.prefixProduct[self.index]=self.currProduct
            self.index+=1
    def getProduct(self, k: int) -> int:
        print(self.prefixProduct)
        if self.index<k:
            return 0
        
        if k == self.index: 
                return self.prefixProduct[self.index - 1]
        return (self.prefixProduct[self.index-1]//self.prefixProduct[self.index-k-1])
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n=n
        self.discount=discount
        self.products=products
        self.prices=prices
        self.count=0
        self.hm=dict(zip(products,prices))

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count+=1
        total=0
        for i in range(len(product)):
            total+=self.hm[product[i]]*amount[i]
        if self.count%self.n==0:
            total*=(100-self.discount)/100.0
        return total



        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
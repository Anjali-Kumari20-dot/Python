class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ordr2):
       return self.price > ordr2.price 

ordr1 = Order("Chips", 20)
ordr2 = Order("Tea", 15)
ordr3 = ordr1 > ordr2
print(ordr3)

class Item:
    def __init__(self,n='', p=0):
        self.name = n
        self.price = p
      
    def itemDetails(self,name,price):
        return name, price
    
    

class ShoppingCart:
    def __init__(self,no='',po=0):
        self.nameI = no
        self.priceI = po
        self.name_cart = []
        self.price_cart = []
        

    def add(self,nameI,priceI):
        no, po = Item.itemDetails(self,nameI, priceI)

        self.name_cart =  self.name_cart + [no]
        self.price_cart = self.price_cart + [po]
        print("your cart containes:",self.name_cart)

        return self.name_cart, self.price_cart

    
    def totalPrice(self):
        totalamount = sum(self.price_cart)
        print(totalamount)
        return totalamount


    def len(self):
        no_of_items = len(self.name_cart)
        print("Total cart items: ",no_of_items)
        return no_of_items

        
sc = ShoppingCart()
name_cart, price_cart = sc.add('cereals',10)
name_cart, price_cart = sc.add('Nuts',12)
name_cart, price_cart = sc.add('Bisuits',8)
sc.totalPrice()
sc.len()




    
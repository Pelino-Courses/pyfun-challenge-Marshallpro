class Product: 
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_inv(self, in_bal=10):
        bal = in_bal + self.quantity
        return bal

    def rem_inv(self, in_bal):

        remain = in_bal - self.quantity
        return remain

    def total_v(self):
        total = self.price * self.quantity
        return total  

    def prod_info(self):
        print(f"This is {self.name}. You want {self.quantity} unit(s). Its price is {self.price} per unit.")


# DATA FROM USER
prod = input("Enter product name: ")
price = int(input("Enter product price: "))
if price < 0:
   raise ValueError("price must be positive.")

if price > 0:
    quantity = int(input("Enter quantity: "))

    if quantity > 0:
        item = Product(prod, price, quantity)

        #this method should be called to display all information related to product  you want
        item.prod_info()

        #this method should be called to  add some units in our stock
        print("Inventory after adding:", item.add_inv()) 

        #this method should be called after removing some unit(s)
        print("Remaining inventory after removing purchesed goods:", item.rem_inv(item.add_inv())) 
        
        #this method should be called  after purchesing to know amount to pay
        print("Total value:", item.total_v()) 
    
    else:
       raise ValueError("quantity must be positive.")

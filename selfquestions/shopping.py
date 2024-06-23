#class : product
'''
You are creating a shopping cart application. Design a class called "ShoppingCart" that can hold a list of items.
Each item has a name and price. Implement methods to add items to the cart, remove items from the cart,
calculate the
total price of all items in the cart, and display the contents of the cart.
'''

class ShoppingCart:
    def __init__(self):
        #assuming dict to store the element
        self.items={}

    #adding the item in shopping cart
    def add_item(self, item_name,price):
        if item_name in self.items:
            self.items[item_name] +=price
        else:
            self.items[item_name]=price

    #removing the item in cart
    def remove_item(self,item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"{item_name} is not in shopping list")

    #viewing the info of cart
    def view_cart(self):
        if self.items:
            print("shopping cart :")
            temp=0
            for item,price in self.items.items():
                print(f"{item} : {price}")
                temp+=price
            print(f"total Price is {temp}")
        else:
            print("Cart is empty")



cart=ShoppingCart()
cart.add_item("Tshirt", 500)
cart.add_item("Jeans",999)
cart.add_item("Shirt",1999)

cart.view_cart()

cart.remove_item("Tshirt")
print("Updated shopping cart: ")
cart.view_cart()








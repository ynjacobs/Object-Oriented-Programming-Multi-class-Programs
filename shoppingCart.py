from product import Product

class ShoppingCart:

    def __init__(self):
        self.products = []

    def __str__(self):
       return 'Your cart has:\n '+ '\n'.join(str(product) for product in self.products)
        
        

    def add_to_cart(self, product):
        self.products.append(product)
        return "you have added {} to your cart".format(product.name)

    def remove_from_cart(self, product):
        self.products.remove(product)
        return "you have removed {} to your cart".format(product.name)
    
    def total_before_tax(self):
        total_price = 0 
        for product in self.products:
            total_price += product.base_price
        return total_price

    def after_tax(self):
        total = 0 
        for product in self.products:
            total += product.calculate()
        return total

    def most_expensive(self):
        compare = 0
        for product in self.products:
            compare = max(product.base_price, compare)
        return compare

apple = Product('apple', 2, 0.13)
pear = Product('pear', 3, 0.13)
shopping_cart = ShoppingCart()
print(shopping_cart.add_to_cart(apple))
shopping_cart.add_to_cart(pear)
# shopping_cart.remove_from_cart(apple)

print('your total is $', shopping_cart.total_before_tax())
print('your total after tax is $', shopping_cart.after_tax())
print("the most expensive price is ",shopping_cart.most_expensive())



print(shopping_cart)
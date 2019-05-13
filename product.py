class Product:

    def __init__(self, name, base_price, tax_rate):
        self.name = name
        self.base_price = base_price
        self.tax_rate = tax_rate

    def __str__(self):
        return "{} ".format(self.name)

    def calculate(self):
        total_price = (self.base_price * self.tax_rate) * 10
        return total_price

# my_product = Product('apple', 3, 0.13)
# # print(my_product)
# total_price = my_product.calculate(3, 0.13)
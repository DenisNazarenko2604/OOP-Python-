

class Product:
    def __init__(self, name, price, aveliable):
        self.name = name
        self.price = price
        self.presence = aveliable

class Cart:
    def add_product(self, product):
        if product.available:
            self.items.append(product)
            print(f"Product '{product.name}' add to cart")
        else:
            print(f"Product '{product.name}' is not available")

    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)
            print(f"Product '{product.name}' delete from the cart")
        else:
            print(f"Product '{product.name}' is not available")

    def total_price(self):
        total = sum(p.price for p in self.items)
        return total

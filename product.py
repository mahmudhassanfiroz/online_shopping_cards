
class Product:
    def __init__(self, name, price, stock, reorder_level, reorder_quantity):
        self.name = name
        self.price = price
        self.stock = stock
        self.reorder_level = reorder_level
        self.reorder_quantity = reorder_quantity

    def update_stock(self, quantity):
        self.stock += quantity

    def get_price(self, discount=0):
        if discount < 0 or discount > 100:
            raise ValueError("Discount must be between 0 and 100 perecet.")
        final_price = self.price * (1 - discount / 100)
        return final_price
        # return self.price
    
    def is_in_stock(self):
        return self.stock > 0

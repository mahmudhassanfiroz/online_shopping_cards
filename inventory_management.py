
class Inventory:
    def __init__(self):
        self.products = {}
    
    def add_product(self, product):
        if product.name in self.products:
            print(f"Product {product.name} already exists in the inventory.")
            self.update_stock(product.name, product.stock)
        else:
            self.products[product.name] = product
        # self.products[product.name] = product
    
    def update_stock(self, product_name, quantity):
        if product_name in self.products:
            self.products[product_name].update_stock(quantity)
        else:
            raise KeyError(f"Product '{product_name}', not found in inventory.")

    def check_reorder(self, product_name):
        if product_name not in self.products:
            raise KeyError(f"Product '{product_name}' not found in inventory.")
        product = self.products[product_name]
        if product.stock < product.reorder_level:
            print(f"Warning: {product_name} stock is below reorder level! consider reordering {self.reorder_quantity} units.")
        else:
            print(f"{product_name} stock is above reorder level.")
    
    def reorder(self, product_name):
        if product_name not in self.products:
            raise KeyError(f"Product '{product_name}' not found in inventory.")
        product = self.products[product_name]
        if product.stock < product.reorder_level:
            print(f"Reordering {product.reorder_quantity} units of {product_name}.")
            product.update_stock(product.reorder_quantity)
        else:
            print(f"{product_name} has sufficient stock. No reorder needed.")
    
    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
        else:
            raise KeyError(f"Product '{product_name}' not found in inventory.")
    
    def list_products(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            for product in self.products.values():
                print(product)



class ShoppingCart:
    def __init__(self):
        self.products = {}  # Initialize as a dictionary
    
    def add_product(self, product, quantity):
        if product.name in self.products:
            self.products[product.name]['quantity'] += quantity
        else:
            self.products[product.name] = {
                'product': product,  # Store the product object
                'quantity': quantity
            }
    
    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
    
    def calculate_total(self):
        total = 0
        for item in self.products.values():
            total += item['product'].get_price() * item['quantity']
        return total

    def update_quantity(self, product_name, quantity):
        if product_name in self.products:
            if quantity <= 0:
                self.remove_product(product_name)
            else:
                self.products[product_name]['quantity'] = quantity
        else:
            raise ValueError(f"Product '{product_name}' not found in the cart.")

    def display_cart(self):
        print("Cart Contents:")
        for item, details in self.products.items():
            print(f"{item}: {details['quantity']}")


from product import Product
from shopping_cart import ShoppingCart
from inventory_management import Inventory

inventory = Inventory()
product = Product("Laptop", 10000, 2, 2, 1)
product1 = Product("Headphones", 50, 2, 2, 1)

print("Stock: ", product.update_stock(1), "Price: ", product.get_price())
print("Stock: ", product.update_stock(1), "Price: ", product.get_price())

cart = ShoppingCart()
cart.add_product(product, 1)
cart.add_product(product1, 1)
cart.display_cart()
inventory.add_product(product)
inventory.add_product(product1)
inventory.list_products()
inventory.check_reorder("Laptop")
inventory.reorder("Laptop")
inventory.list_products()
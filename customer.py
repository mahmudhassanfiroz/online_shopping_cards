
from shopping_cart import ShoppingCart 
from payment import Payment
from order import Order
class Customer:
    def __init__(self, name, email):
        self.name = name 
        self.email = email
        self.cart = ShoppingCart()
        self.order_list = []
    
    def add_to_cart(self, product, quantity):
        self.cart.add_product(product, quantity)
    
    def view_cart(self):
        for item, details in self.cart.items.items():
            print(f"Product: {item}, Quantity: {details['quantity']}")
    
    def checkout(self):
        total = self.cart.calculate_total()
        print(f"Total amount to be paid: {total}")
        # Payment Process 
        order = Order(self.cart)
        self.order_list.append(order)
        payment = Payment()
        payment.process_payment(total)
        order.generate_invoice()
    
    def checkout(self, promo_code=None):
        """
        Processes the checkout, generates an order, and handles payment.
        
        Args:
            promo_code (PromoCode, optional): A promo code to apply during checkout.
        """
        total = self.cart.calculate_total()
        print(f"Total amount to be paid: {total:.2f}")
        
        if promo_code:
            if promo_code.is_valid():
                total = promo_code.apply_promo_code(total)
                print(f"Promo code applied! New total: {total:.2f}")
            else:
                print("Promo code is invalid or expired.")
        
        # Payment Process 
        payment = Payment()
        if payment.process_payment(total, 'CreditCard'):  # Assuming CreditCard for simplicity
            order = Order(self.cart, promo_code)
            self.order_list.append(order)
            order.generate_invoice()
            self.cart = ShoppingCart()  # Clear cart after successful checkout
            
            # Update loyalty points
            self.loyalty_points += int(total // 10)  # Example: 1 point per $10 spent
            print(f"Loyalty points earned: {int(total // 10)}")
        else:
            print("Payment failed. Please try again.")
    
    def view_order_history(self):
        for order in self.order_list:
            print(f"Order ID: {order.order_id}, Total: {order.total}")


        


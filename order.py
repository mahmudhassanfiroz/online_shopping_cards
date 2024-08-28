
from datetime import datetime
import uuid

class Order:
    def __init__(self, cart, promo_code=None):
        self.order_id = uuid.uuid4()
        self.products = cart.items
        self.original_total = cart.calculate_total()
        self.promo_code = promo_code
        self.discounted_total = self.apply_promo_code() if promo_code else self.original_total
        self.status = 'Pending'
        self.date = datetime.now()
    
    def apply_promo_code(self):
        """
        Applies the promo code to the total order amount.
        
        Returns:
            float: The new total after applying the promo code.
        """
        if self.promo_code and self.promo_code.is_valid():
            return self.promo_code.apply_promo_code(self.original_total)
        else:
            return self.original_total

    # def generate_invoice(self):
    #     print(f"Order Id: {self.order_id}")
    #     for item, details in self.products.items():
    #         print(f"Product: {item}, Quantity: {details['quantity']}, Price: {details['product'].get_price()}")
    #     print(f"Total: {self.total}")

    def generate_invoice(self, save_to_file=False, filename=None):
        """
        Generates and optionally saves the order invoice.
        
        Args:
            save_to_file (bool, optional): If True, the invoice will be saved to a file.
            filename (str, optional): The filename for saving the invoice. If not provided, a default filename is generated.
        """
        invoice = []
        invoice.append(f"Order Id: {self.order_id}")
        invoice.append(f"Date: {self.date.strftime('%Y-%m-%d %H:%M:%S')}")
        invoice.append(f"Status: {self.status}")
        invoice.append("\nItems:")
        
        for item, details in self.products.items():
            line = f"Product: {item}, Quantity: {details['quantity']}, Price: {details['product'].get_price():.2f}"
            invoice.append(line)
        
        invoice.append(f"\nOriginal Total: {self.original_total:.2f}")
        
        if self.promo_code:
            invoice.append(f"Promo Code: {self.promo_code.code} applied, New Total: {self.discounted_total:.2f}")
        else:
            invoice.append(f"Total: {self.discounted_total:.2f}")
        
        invoice_content = "\n".join(invoice)
        print(invoice_content)
        
        if save_to_file:
            if not filename:
                filename = f"Invoice_{self.order_id}.txt"
            with open(filename, "w") as file:
                file.write(invoice_content)
            print(f"Invoice saved to {filename}")
    
    def update_status(self, new_status):
        """
        Updates the order status.
        
        Args:
            new_status (str): The new status for the order.
        """
        self.status = new_status


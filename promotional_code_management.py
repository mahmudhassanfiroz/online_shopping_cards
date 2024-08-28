
from datetime import datetime

class PromoCode:
    def __init__(self, code, discount, validity):
        self.code = code
        self.discount = discount
        self.validity = validity
    
    def is_valid(self):
        return datetime.now() <= self.validity

    def apply_promo_code(self, price):
        if self.is_valid():
            return self.discount.apply_discount(price)
        else:
            print("Promo code is expired or invalid")
            return price


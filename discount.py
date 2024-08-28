
class Discount:
    def __init__(self, discount_type, value):
        if discount_type not in ['percentage', 'fixed_amount']:
            raise ValueError('Invalid discount type')
        if value < 0:
            raise ValueError('Invalid discount value')
        if discount_type == 'percentage' and value > 100:
            raise ValueError('Invalid discount value for percentage discount')
        self.discount_type = discount_type
        self.value = value
    
    def apply_discount(self, price):
        if price < 0:
            raise ValueError('Invalid price')
        if self.discount_type == 'percentage':
            # return price - (price * (self.value/100))
            discount_price = price - (price * (self.value/100))
        elif self.discount_type == 'fixed_amount':
            # return max(0, price - self.value)
            discount_price = max(0, price-self.value)
        else:
            discount_price = price
        # return price
        return round(discount_price, 2)

    def discount_details(self):
        if self.discount_type == 'percentage':
            return f"{self.value}% discount"
        elif self.discount_type == 'fixed_amount':
            return f"${self.value:.2f} discount"
        else:
            return "No discount"


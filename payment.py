
class Payment:
    def __init__(self):
        """
        Initializes the Payment processor.
        """
        self.supported_methods = ['CreditCard', 'Paypal', 'Bikash', 'Nagod']
    
    def validate_method(self, method):
        """
        Validates if the provided payment method is supported.
        
        Args:
            method (str): The payment method to validate.
        
        Returns:
            bool: True if the method is supported, False otherwise.
        """
        if method not in self.supported_methods:
            print(f"Error: Payment method '{method}' is not supported.")
            return False
        return True
    def process_payment(self, amount, method):
        #print(f"Processing payment of {amount}...")
        # Simulate payment processing
        #print("Payment Successful!")
        if method == 'CreditCard':
            print(f"Processing credit card payment of {amount}...")
        elif method == 'Paypal':
            print(f"Processing Paypal payment of {amount}....")
        elif method == 'Bikas':
            print(f"Processing Bikash Payment of {amount}")
        elif method == 'Nagot':
            print(f"Processing Nagod payment of {amount}....")
        # Simulate payment processing
        print("Payment Successful!")




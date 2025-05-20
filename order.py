class Order:
    all = []

    def __init__(self, customer, beverage, size, price):
        self.customer = customer
        self.beverage = beverage
        self.size = size
        self.price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if not isinstance(value, str):
            raise ValueError("Customer name must be a string.")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Customer name must be between 1 and 15 characters long.")
        self._customer = value

    @property
    def beverage(self):
        return self._beverage

    @beverage.setter
    def beverage (self, value):
        if not isinstance(value, str):
            raise ValueError("Beverage name must be a string.")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Beverage name must be between 1 and 15 characters long.")
        self._beverage = value   

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, str):
            raise ValueError("Size must be a string.")
        if value not in ["small", "medium", "large"]:
            raise ValueError("Size must be 'small', 'medium', or 'large'.")
        self._size = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be a number.")
        if value < 0:
            raise ValueError("Price must be a positive number.")
        self._price = value       

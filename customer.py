from order import Order

class Customer:
    def __init__(self, name):
        self._validate_name(name)
        self._name = name

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be between 1 and 15 characters long.")

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        # Return unique coffees this customer ordered
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        # Create a new order associated with this customer and given coffee and price
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        spending = {}
        for order in Order.all:
            if order.coffee == coffee:
                spending[order.customer] = spending.get(order.customer, 0) + order.price
        if not spending:
            return None
        # Return customer with max spending on this coffee
        return max(spending, key=spending.get)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value

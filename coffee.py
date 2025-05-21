from order import Order

class Coffee:
    def __init__(self, name):
        self._validate_name(name)
        self._name = name

    def _validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        # Return unique customers who ordered this coffee
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value

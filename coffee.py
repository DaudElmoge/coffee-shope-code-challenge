from order import Order

class Coffee:
    def __init__(self,name):
        self.name=name
        self._validate_name(name)

    def _validate_name(self,name):
        if not isinstance(name,str):
            raise Exception("Name must be a string.")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long.")
    
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return [order.customer for order in self.orders()]

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        self._validate_name(value)
        self._name=value
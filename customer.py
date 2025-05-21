from order import Order

class Customer:
    def __init__(self,name):
        self.name=name
        self._validate_name(name)

    def _validate_name(self,name):
        if not isinstance (name,str):
            raise Exception ("Name must be a string.")
        if len(name) < 1 or len (name) > 15:#checks if string is not empty and less than 15 characters
            raise ValueError("Name must be between 1 and 15 characters long.")

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffee(self):
        return [order.coffee for order in self.orders()]
    
    def create_order(self,coffee,size,price):
        return Order(self,coffee,size,price)

    @classmethod
    def most_aficionado(cls,coffee):
        customer_spending = {}
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer not in customer_spending:
                    customer_spending[order.customer] = 0
                customer_spending[order.customer] += order.price
        if not customer_spending:
            return None
        return max(customer_spending, key=customer_spending.get)
    #checks who spent the most on a specific coffee
    #returns the customer who spent the most on a specific coffee


    @property
    def name (self):
        return self._name
    @name.setter  
    def name(self,value):
        self._validate_name(value)
        self._name=value      
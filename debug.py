from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Daud")
c2 = Customer("Aisha")
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

c1.create_order(coffee1, 5.0)
c1.create_order(coffee2, 6.0)
c2.create_order(coffee1, 7.0)

print(coffee1.customers())  # List of unique customers for Espresso
print(coffee1.average_price())  # Average price for Espresso
print(Customer.most_aficionado(coffee1).name)  # Customer who spent most on Espresso

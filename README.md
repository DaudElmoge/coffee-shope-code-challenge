# ☕ Coffee Shop Project

This is a Python assignment that models a coffee shop using object-oriented programming. It includes three main classes: `Customer`, `Coffee`, and `Order`.

## 🧠 Relationships

- A **Customer** can place many **Orders**.
- A **Coffee** can have many **Orders**.
- An **Order** connects one **Customer** and one **Coffee** (many-to-many via Order).

## 📁 Files

- `customer.py` – Customer class with name validation and order methods
- `coffee.py` – Coffee class with order tracking and average price
- `order.py` – Order class that connects customers and coffees
- `debug.py` – For testing the code interactively

## ✅ Features

- Create customers and coffees
- Place orders with price and size
- Get all orders by a customer or for a coffee
- Find who spent the most on a specific coffee

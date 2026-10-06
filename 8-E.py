# Shopping cart class

class ShoppingCart:

    def __init__(self):
        self.items = []

    # Add an item
    def add_item(self, name, price):
        self.items.append((name, price))

    # Remove an item
    def remove_item(self, name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                break

    # Calculate total price
    def total_price(self):
        total = 0
        for item in self.items:
            total = total + item[1]
        return total


# Create shopping cart object
cart = ShoppingCart()

# Add items
cart.add_item("Pen", 20)
cart.add_item("Book", 100)
cart.add_item("Bag", 500)

# Remove an item
cart.remove_item("Pen")

# Display total price
print("Total Price:", cart.total_price())
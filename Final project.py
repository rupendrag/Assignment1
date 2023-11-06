class FoodItem:
    food_id_counter = 1

    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = FoodItem.food_id_counter
        FoodItem.food_id_counter += 1
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        self.food_items.append(food_item)

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for item in self.food_items:
            if item.food_id == food_id:
                item.name = name
                item.quantity = quantity
                item.price = price
                item.discount = discount
                item.stock = stock
                break

    def view_food_items(self):
        for item in self.food_items:
            print(f"ID: {item.food_id}, Name: {item.name}, Quantity: {item.quantity}, Price: {item.price}, Discount: {item.discount}, Stock: {item.stock}")

    def remove_food_item(self, food_id):
        self.food_items = [item for item in self.food_items if item.food_id != food_id]

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

    def place_order(self, food_items):
        total_price = 0
        selected_items = []

        for food_id in food_items:
            for item in admin.food_items:
                if item.food_id == food_id and item.stock > 0:
                    total_price += item.price
                    selected_items.append(item)
                    item.stock -= 1

        if total_price > 0:
            self.orders.append(selected_items)
            print("Order placed successfully!")
            print("Ordered Items:")
            for item in selected_items:
                print(f"{item.name} ({item.quantity}) [INR {item.price}]")
            print(f"Total Amount: INR {total_price}")
        else:
            print("No items selected or items are out of stock.")

    def view_order_history(self):
        for i, order in enumerate(self.orders, 1):
            print(f"Order {i}:")
            for item in order:
                print(f"{item.name} ({item.quantity}) [INR {item.price}]")
            print()

    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

admin = Admin()
user = User("John Doe", "123-456-7890", "john@example.com", "123 Main St", "password")

# Admin adds food items
admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 10)
admin.add_food_item("Vegan Burger", "1 Piece", 320, 0, 5)
admin.add_food_item("Truffle Cake", "500gm", 900, 0, 8)

# User places an order
user.place_order([2, 3])

# Admin views food items
admin.view_food_items()

# User views order history
user.view_order_history()

# User updates their profile
user.update_profile("John Smith", "987-654-3210", "john.smith@example.com", "456 Oak St", "newpassword")
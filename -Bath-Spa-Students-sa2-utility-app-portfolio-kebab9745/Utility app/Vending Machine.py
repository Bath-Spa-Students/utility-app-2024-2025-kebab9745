# Vending Machine Program

# Define vending machine items
items = {
    "NCD_1": {"name": "Bottled Water", "price": 3.0, "stock": 5, "category": "Non-Carbonated Drinks"},
    "NCD_2": {"name": "Orange Juice", "price": 5.5, "stock": 5, "category": "Non-Carbonated Drinks"},
    "CD_1": {"name": "Coca-Cola", "price": 4.0, "stock": 5, "category": "Carbonated Drinks"},
    "CD_2": {"name": "Sprite", "price": 4.0, "stock": 5, "category": "Carbonated Drinks"},
    "CFD_1": {"name": "Espresso", "price": 10.0, "stock": 5, "category": "Caffeinated Drinks"},
    "CFD_2": {"name": "Cappuccino", "price": 12.0, "stock": 5, "category": "Caffeinated Drinks"},
    "S_1": {"name": "Lays Classic Chips", "price": 6.5, "stock": 5, "category": "Snacks"},
    "S_2": {"name": "Pringles Sour Cream", "price": 9.0, "stock": 5, "category": "Snacks"},
    "C_1": {"name": "KitKat", "price": 3.5, "stock": 5, "category": "Candy"},
    "C_2": {"name": "Mentos Mint", "price": 2.0, "stock": 5, "category": "Candy"},
}

cart = []  # Cart to hold selected items

# Function to display items
def display_items():
    print("\nItems in the vending machine:\n")
    categories = {}
    for code, item in items.items():
        if item["category"] not in categories:
            categories[item["category"]] = []
        categories[item["category"]].append((code, item))
    for category, items_list in categories.items():
        print(f"{category}:")
        for code, item in items_list:
            print(f"  {code} - {item['name']}: AED {item['price']} (In stock: {item['stock']})")
    print("\nOptions: Type a code to add an item to your cart, 'checkout' to finish, or 'quit' to exit.")

# Function to handle checkout
def handle_checkout():
    if not cart:
        print("Your cart is empty! Please add items before checking out.")
    else:
        # Calculate total cost
        total_cost = sum(items[code]["price"] for code in cart)
        print(f"Your total is: AED {total_cost:.2f}")
        
        # Handle payment
        try:
            money_inserted = float(input("Insert money (in AED): "))
        except ValueError:
            print("Invalid input. Please insert a valid amount.")
            return
        
        if money_inserted >= total_cost:
            change = money_inserted - total_cost
            print(f"Thank you! Your items have been dispensed.")
            print(f"Your change is: AED {change:.2f}")
            
            # Update stock
            for code in cart:
                items[code]["stock"] -= 1
            
            cart.clear()  # Clear the cart after checkout
        else:
            print("Not enough money inserted. Please add more or remove items.")

# Main program loop
while True:
    display_items()
    user_input = input("Your choice: ").strip()

    if user_input.lower() == "quit":
        print("Thank you for using the vending machine. Goodbye!")
        break
    elif user_input.lower() == "checkout":
        handle_checkout()
    elif user_input in items:
        item = items[user_input]
        if item["stock"] > 0:
            cart.append(user_input)
            print(f"Added {item['name']} to your cart.")
        else:
            print(f"Sorry, {item['name']} is out of stock.")
    else:
        print("Invalid code. Please try again.")

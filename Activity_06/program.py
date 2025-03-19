class Item:
    def __init__(self, item_id, name, description, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, item_id, name, description, price):
        if item_id in self.items:
            print("Error: Item ID already exists.")
            return
        
        try:
            item = Item(item_id, name, description, price)
            self.items[item_id] = item
            print("Item added successfully.")
        except ValueError as e:
            print("Error:", e)

    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)

    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            print("Error: Item not found.")
            return
        
        item = self.items[item_id]
        if name:
            item.name = name
        if description:
            item.description = description
        if price is not None:
            if price < 0:
                print("Error: Price cannot be negative.")
                return
            item.price = price
        print("Item updated successfully.")

    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully.")
        else:
            print("Error: Item not found.")


def main():
    manager = ItemManager()
    while True:
        print("\nItem Management Menu:")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                item_id = input("Enter item ID: ")
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))
                manager.create_item(item_id, name, description, price)
            except ValueError:
                print("Error: Invalid price. Please enter a numeric value.")
        elif choice == '2':
            manager.read_items()
        elif choice == '3':
            item_id = input("Enter item ID to update: ")
            name = input("Enter new name (leave blank to keep current): ") or None
            description = input("Enter new description (leave blank to keep current): ") or None
            try:
                price_input = input("Enter new price (leave blank to keep current): ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name, description, price)
            except ValueError:
                print("Error: Invalid price. Please enter a numeric value.")
        elif choice == '4':
            item_id = input("Enter item ID to delete: ")
            manager.delete_item(item_id)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
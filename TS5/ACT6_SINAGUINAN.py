class Item:
    def __init__(self, item_id, name, description, price):
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
            raise ValueError("Item ID already exists.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.items[item_id] = Item(item_id, name, description, price)

    def read_item(self, item_id):
        return self.items.get(item_id, None)

    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            raise ValueError("Item ID does not exist.")
        if price is not None and price < 0:
            raise ValueError("Price cannot be negative.")
        
        item = self.items[item_id]
        if name is not None:
            item.name = name
        if description is not None:
            item.description = description
        if price is not None:
            item.price = price

    def delete_item(self, item_id):
        if item_id not in self.items:
            raise ValueError("Item ID does not exist.")
        del self.items[item_id]

    def list_items(self):
        return list(self.items.values())


def main():
    manager = ItemManager()

    while True:
        print("\nItem Management Menu:")
        print("[C] - Create Item")
        print("[R] - Read Item")
        print("[U] - Update Item")
        print("[D] - Delete Item")
        print("[L] - List Items")
        print("[Q] - Quit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'Q':
            print("Exiting the program.")
            break

        try:
            if choice == 'C':
                item_id = input("Enter item ID: ")
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))
                manager.create_item(item_id, name, description, price)
                print("Item created successfully.")

            elif choice == 'R':
                item_id = input("Enter item ID to read: ")
                item = manager.read_item(item_id)
                if item:
                    print(item)
                else:
                    print("Item not found.")

            elif choice == 'U':
                item_id = input("Enter item ID to update: ")
                name = input("Enter new item name (leave blank to keep current): ")
                description = input("Enter new item description (leave blank to keep current): ")
                price_input = input("Enter new item price (leave blank to keep current): ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name if name else None, description if description else None, price)
                print("Item updated successfully.")

            elif choice == 'D':
                item_id = input("Enter item ID to delete: ")
                manager.delete_item(item_id)
                print("Item deleted successfully.")

            elif choice == 'L':
                items = manager.list_items()
                if items:
                    for item in items:
                        print(item)
                else:
                    print("No items available.")

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

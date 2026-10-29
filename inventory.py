class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)

    def update_stock(self, quantity):
        if self.__stock + quantity < 0:
            print("Error: Stock cannot be negative.")
        else:
            self.__stock += quantity
            print("Stock updated successfully.")

    def display_information(self):
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        if not self.products:
            print("Inventory is empty.")
            return

        for product in self.products:
            product.display_information()
            print("-" * 20)

    def search_product(self, product_id):
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None


class FileManager:
    @staticmethod
    def save_inventory(inventory):
        with open("inventory.txt", "w") as file:
            for product in inventory.products:
                file.write(
                    f"{product.get_product_id()},"
                    f"{product.get_name()},"
                    f"{product.get_price()},"
                    f"{product.get_stock()}\n"
                )
        print("Inventory saved successfully.")

    @staticmethod
    def load_inventory(inventory):
        inventory.products.clear()

        try:
            with open("inventory.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")

                    product = Product(
                        data[0],
                        data[1],
                        float(data[2]),
                        int(data[3])
                    )

                    inventory.add_product(product)

            print("Inventory loaded successfully.")

        except FileNotFoundError:
            print("No inventory file found.")


def menu():
    inventory = Inventory()

    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. Save Inventory")
        print("6. Load Inventory")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            stock = int(input("Enter Initial Stock: "))

            product = Product(product_id, name, price, stock)
            inventory.add_product(product)

            print("Product added successfully!")

        elif choice == "2":
            inventory.display_products()

        elif choice == "3":
            product_id = input("Enter Product ID to search: ")

            product = inventory.search_product(product_id)

            if product:
                product.display_information()
            else:
                print("Product not found.")

        elif choice == "4":
            product_id = input("Enter Product ID: ")

            product = inventory.search_product(product_id)

            if product:
                quantity = int(input("Enter quantity to add/remove: "))
                product.update_stock(quantity)
            else:
                print("Product not found.")

        elif choice == "5":
            FileManager.save_inventory(inventory)

        elif choice == "6":
            FileManager.load_inventory(inventory)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


menu()
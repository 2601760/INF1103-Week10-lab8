class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)

    # Getters
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # Encapsulated stock update
    def update_stock(self, quantity):
        if self.__stock + quantity < 0:
            print("Error: Stock cannot be negative.")
        else:
            self.__stock += quantity
            print("Stock updated successfully.")

    def display_information(self):
        print("\n------------------------")
        print(f"Product ID : {self.__product_id}")
        print(f"Name       : {self.__name}")
        print(f"Price      : ${self.__price:.2f}")
        print(f"Stock      : {self.__stock}")
        print("------------------------")


inventory = []


def add_product():
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    stock = int(input("Enter Initial Stock: "))

    product = Product(product_id, name, price, stock)
    inventory.append(product)

    print("Product added successfully!")


def display_products():
    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    print("\n=== INVENTORY ===")
    for product in inventory:
        product.display_information()


def search_product():
    product_id = input("Enter Product ID to search: ")

    for product in inventory:
        if product.get_product_id() == product_id:
            print("Product found:")
            product.display_information()
            return

    print("Product not found.")


def update_stock():
    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product.get_product_id() == product_id:
            quantity = int(input("Enter quantity to add/remove: "))
            product.update_stock(quantity)
            return

    print("Product not found.")


def save_inventory():
    try:
        with open("inventory.txt", "w") as file:
            for product in inventory:
                file.write(
                    f"{product.get_product_id()},"
                    f"{product.get_name()},"
                    f"{product.get_price()},"
                    f"{product.get_stock()}\n"
                )

        print("Inventory saved successfully.")

    except Exception as e:
        print("Error saving inventory:", e)


def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            inventory.clear()

            for line in file:
                data = line.strip().split(",")

                product = Product(
                    data[0],
                    data[1],
                    float(data[2]),
                    int(data[3])
                )

                inventory.append(product)

        print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("No inventory file found.")


def menu():
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
            add_product()

        elif choice == "2":
            display_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_stock()

        elif choice == "5":
            save_inventory()

        elif choice == "6":
            load_inventory()

        elif choice == "7":
            print("Thank you for using the Inventory Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


menu()
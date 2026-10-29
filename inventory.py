class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)

    def update_stock(self, quantity):
        self.__stock += quantity

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


inventory = []


def add_product():
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    stock = int(input("Enter Stock Quantity: "))

    product = Product(product_id, name, price, stock)
    inventory.append(product)

    print("Product added successfully!")


def display_products():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\n=== INVENTORY ===")
    for product in inventory:
        product.display_information()
        print("-" * 20)


def search_product():
    search_id = input("Enter Product ID to search: ")

    for product in inventory:
        if product.get_product_id() == search_id:
            print("\nProduct Found:")
            product.display_information()
            return

    print("Product not found.")


def update_product_stock():
    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product.get_product_id() == product_id:
            quantity = int(input("Enter stock change (+/-): "))
            product.update_stock(quantity)
            print("Stock updated successfully!")
            return

    print("Product not found.")


def save_inventory():
    file = open("inventory.txt", "w")

    for product in inventory:
        file.write(
            f"{product.get_product_id()},"
            f"{product.get_name()},"
            f"{product.get_price()},"
            f"{product.get_stock()}\n"
        )

    file.close()
    print("Inventory saved successfully!")


def load_inventory():
    try:
        file = open("inventory.txt", "r")

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

        file.close()
        print("Inventory loaded successfully!")

    except FileNotFoundError:
        print("No inventory file found.")


def menu():
    while True:
        print("\n===== INVENTORY SYSTEM =====")
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
            update_product_stock()

        elif choice == "5":
            save_inventory()

        elif choice == "6":
            load_inventory()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


menu()
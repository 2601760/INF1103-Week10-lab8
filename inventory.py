# Product Class
class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        if self.__stock + quantity >= 0:
            self.__stock += quantity
            return True
        return False

    def display_information(self):
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")


# Inventory Class
class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            product.display_information()
            print("-" * 20)

    def get_products(self):
        return self.__products


# File Handling Functions
def save_inventory(inventory):
    with open("inventory.txt", "w") as file:
        for product in inventory.get_products():
            file.write(
                f"{product.get_product_id()},"
                f"{product.get_name()},"
                f"{product.get_price()},"
                f"{product.get_stock()}\n"
            )

    print("Inventory saved successfully.")


def load_inventory(inventory):
    try:
        inventory.get_products().clear()

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

    except FileNotFoundError:
        pass


# Main Program
def main():
    inventory = Inventory()

    load_inventory(inventory)

    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock Quantity: "))

            product = Product(product_id, name, price, stock)
            inventory.add_product(product)

            print("Product added successfully.")

        elif choice == "3":
            product_id = input("Enter Product ID: ")

            product = inventory.search_product(product_id)

            if product:
                quantity = int(input("Enter stock change (+/-): "))

                if product.update_stock(quantity):
                    print("Stock updated successfully.")
                else:
                    print("Stock cannot be negative.")
            else:
                print("Product not found.")

        elif choice == "4":
            product_id = input("Enter Product ID: ")

            product = inventory.search_product(product_id)

            if product:
                product.display_information()
            else:
                print("Product not found.")

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            save_inventory(inventory)
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()
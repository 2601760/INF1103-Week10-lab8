import json
from abc import ABC, abstractmethod


# =====================================
# Abstract Product Class
# =====================================
class Product(ABC):
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
        print(f"Product ID : {self.__product_id}")
        print(f"Name       : {self.__name}")
        print(f"Price      : ${self.__price:.2f}")
        print(f"Stock      : {self.__stock}")

    @abstractmethod
    def get_fulfilment_info(self):
        pass


# =====================================
# Physical Product
# =====================================
class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = float(weight)

    def display_information(self):
        super().display_information()
        print(f"Weight     : {self.__weight} kg")

    def get_fulfilment_info(self):
        return f"Shipping weight: {self.__weight} kg"


# =====================================
# Digital Product
# =====================================
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = float(download_size)

    def display_information(self):
        super().display_information()
        print(f"Download Size : {self.__download_size} MB")

    def get_fulfilment_info(self):
        return f"Download size: {self.__download_size} MB"


# =====================================
# Inventory Class
# =====================================
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

        print("\n=== PRODUCT LIST ===")

        for product in self.__products:
            product.display_information()
            print(product.get_fulfilment_info())
            print("-" * 30)

    def get_products(self):
        return self.__products


# =====================================
# Save Inventory
# =====================================
def save_inventory(inventory):
    data = []

    for product in inventory.get_products():
        data.append({
            "product_id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        })

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully.")


# =====================================
# Load Inventory
# =====================================
def load_inventory(inventory):
    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        inventory.get_products().clear()

        for item in data:
            product = PhysicalProduct(
                item["product_id"],
                item["name"],
                item["price"],
                item["stock"],
                1.0
            )

            inventory.add_product(product)

    except FileNotFoundError:
        print("No inventory.json found. Starting with empty inventory.")


# =====================================
# Main Program
# =====================================
def main():
    inventory = Inventory()

    load_inventory(inventory)

    print("\n=== Physical Product Test ===")
    physical_product = PhysicalProduct(
        "P001",
        "Laptop",
        1200.00,
        15,
        2.5
    )

    physical_product.display_information()
    print(physical_product.get_fulfilment_info())

    print("\n" + "-" * 30 + "\n")

    print("=== Digital Product Test ===")
    digital_product = DigitalProduct(
        "D001",
        "Microsoft Office",
        199.99,
        100,
        3500
    )

    digital_product.display_information()
    print(digital_product.get_fulfilment_info())

    inventory.add_product(physical_product)
    inventory.add_product(digital_product)

    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Display All Products")
        print("2. Add Physical Product")
        print("3. Add Digital Product")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock Quantity: "))
            weight = float(input("Enter Weight (kg): "))

            inventory.add_product(
                PhysicalProduct(
                    product_id,
                    name,
                    price,
                    stock,
                    weight
                )
            )

            print("Physical product added successfully.")

        elif choice == "3":
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock Quantity: "))
            download_size = float(input("Enter Download Size (MB): "))

            inventory.add_product(
                DigitalProduct(
                    product_id,
                    name,
                    price,
                    stock,
                    download_size
                )
            )

            print("Digital product added successfully.")

        elif choice == "4":
            product_id = input("Enter Product ID: ")

            product = inventory.search_product(product_id)

            if product:
                product.display_information()
                print(product.get_fulfilment_info())
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

"1"
main()
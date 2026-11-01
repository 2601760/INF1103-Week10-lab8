from abc import ABC, abstractmethod


# =====================================
# CanBeShipped Interface
# =====================================
class CanBeShipped(ABC):

    @abstractmethod
    def calculate_shipping_cost(self):
        pass


# =====================================
# Abstract Product Class
# =====================================
class Product(ABC):

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)

    def display_information(self):
        print(f"Product ID : {self.__product_id}")
        print(f"Name       : {self.__name}")
        print(f"Price      : ${self.__price:.2f}")
        print(f"Stock      : {self.__stock}")

    @abstractmethod
    def get_fulfilment_info(self):
        pass


# =====================================
# PhysicalProduct
# =====================================
class PhysicalProduct(Product):

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = float(weight)

    def display_information(self):
        super().display_information()
        print(f"Weight     : {self.__weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__weight * 5.00


# =====================================
# DigitalProduct
# =====================================
class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = float(download_size)

    def display_information(self):
        super().display_information()
        print(f"Download Size : {self.__download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."


# =====================================
# Main Test Program
# =====================================
def main():

    print("=== Physical Product 1 ===")
    product1 = PhysicalProduct(
        "P001",
        "Laptop",
        1200.00,
        15,
        2.5
    )

    product1.display_information()
    print(product1.get_fulfilment_info())
    print(f"Shipping Cost : ${product1.calculate_shipping_cost():.2f}")

    print("\n" + "-" * 40 + "\n")

    print("=== Physical Product 2 ===")
    product2 = PhysicalProduct(
        "P002",
        "Monitor",
        300.00,
        10,
        5.0
    )

    product2.display_information()
    print(product2.get_fulfilment_info())
    print(f"Shipping Cost : ${product2.calculate_shipping_cost():.2f}")

    print("\n" + "-" * 40 + "\n")

    print("=== Digital Product ===")
    digital = DigitalProduct(
        "D001",
        "Microsoft Office",
        199.99,
        100,
        3500
    )

    digital.display_information()
    print(digital.get_fulfilment_info())


main()
from abc import ABC, abstractmethod


class Shippable(ABC):

    @abstractmethod
    def shipping_fee(self):
        pass


class Vendor:

    def __init__(
        self,
        vendor_id: str,
        company_name: str,
        email_address: str
    ):
        self.vendor_id = vendor_id
        self.company_name = company_name
        self.email_address = email_address

    def show_details(self):
        print(f"Vendor ID     : {self.vendor_id}")
        print(f"Company Name  : {self.company_name}")
        print(f"Email Address : {self.email_address}")


class Item(ABC):

    def __init__(
        self,
        item_id: str,
        item_name: str,
        unit_price: float,
        quantity_available: int,
        vendor: Vendor
    ):
        self.__item_id = item_id
        self.__item_name = item_name
        self.__unit_price = float(unit_price)
        self.__quantity_available = int(quantity_available)
        self.vendor: Vendor = vendor

    def get_item_id(self):
        return self.__item_id

    def get_item_name(self):
        return self.__item_name

    def get_unit_price(self):
        return self.__unit_price

    def get_quantity(self):
        return self.__quantity_available

    def modify_quantity(self, amount):
        if self.__quantity_available + amount >= 0:
            self.__quantity_available += amount
            return True
        return False

    def show_details(self):
        print(f"Item ID   : {self.__item_id}")
        print(f"Name      : {self.__item_name}")
        print(f"Price     : ${self.__unit_price:.2f}")
        print(f"Quantity  : {self.__quantity_available}")

    def show_vendor(self):
        self.vendor.show_details()

    @abstractmethod
    def delivery_details(self):
        pass


class HardwareItem(Item, Shippable):

    def __init__(
        self,
        item_id,
        item_name,
        unit_price,
        quantity_available,
        mass,
        vendor: Vendor
    ):
        super().__init__(
            item_id,
            item_name,
            unit_price,
            quantity_available,
            vendor
        )
        self.__mass = float(mass)

    def get_mass(self):
        return self.__mass

    def show_details(self):
        super().show_details()
        print(f"Mass      : {self.__mass} kg")

    def delivery_details(self):
        return "This item requires physical delivery."

    def shipping_fee(self):
        return self.__mass * 5


class SoftwareItem(Item):

    def __init__(
        self,
        item_id,
        item_name,
        unit_price,
        quantity_available,
        file_size,
        vendor: Vendor
    ):
        super().__init__(
            item_id,
            item_name,
            unit_price,
            quantity_available,
            vendor
        )
        self.__file_size = float(file_size)

    def get_file_size(self):
        return self.__file_size

    def show_details(self):
        super().show_details()
        print(f"File Size : {self.__file_size} MB")

    def delivery_details(self):
        return "This item is delivered digitally."


class Inventory:

    def __init__(self, inventory_name: str):
        self.inventory_name = inventory_name
        self.products: list[Item] = []

    def add_product(self, product: Item):
        self.products.append(product)

    def remove_product(self, product_id: str):
        for product in self.products:
            if product.get_item_id() == product_id:
                self.products.remove(product)
                return True
        return False

    def find_product(self, product_id: str) -> Item | None:
        for product in self.products:
            if product.get_item_id() == product_id:
                return product
        return None

    def display_products(self):
        print(f"\n{self.inventory_name}")

        if not self.products:
            print("No products in inventory.")
            return

        for product in self.products:
            product.show_details()
            print("-" * 30)


def main():

    vendor = Vendor(
        "VEN001",
        "NextGen Solutions",
        "support@nextgensolutions.com"
    )

    laptop = HardwareItem(
        "H001",
        "Gaming Laptop",
        1999.99,
        15,
        2.8,
        vendor
    )

    antivirus = SoftwareItem(
        "S001",
        "Antivirus Pro",
        49.99,
        500,
        350,
        vendor
    )

    print("\n=== ASSOCIATION TEST ===")

    print("\nVendor Through Hardware Item")
    laptop.show_vendor()

    print("\nVendor Through Software Item")
    antivirus.show_vendor()

    del vendor

    print("\nAfter deleting vendor variable:")

    laptop.show_vendor()
    antivirus.show_vendor()

    print("\n=== AGGREGATION TEST ===")

    inventory_a = Inventory("Inventory A")
    inventory_b = Inventory("Inventory B")

    print("\nProduct created before inventory:")
    laptop.show_details()

    inventory_a.add_product(laptop)

    print("\nAdded to Inventory A")
    inventory_a.display_products()

    inventory_a.remove_product("H001")

    print("\nRemoved from Inventory A")

    print("\nProduct still exists:")
    laptop.show_details()

    inventory_b.add_product(laptop)

    print("\nAdded to Inventory B")
    inventory_b.display_products()

    inventory_b.remove_product("H001")

    print("\nRemoved from Inventory B")

    print("\nProduct still exists:")
    laptop.show_details()


main()
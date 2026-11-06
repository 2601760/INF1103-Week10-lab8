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

    print("\nVendor Information Through Hardware Item")
    laptop.show_vendor()

    print("\nVendor Information Through Software Item")
    antivirus.show_vendor()

    print("\nObject IDs")
    print(f"Hardware Item : {id(laptop)}")
    print(f"Software Item : {id(antivirus)}")
    print(f"Vendor From Hardware : {id(laptop.vendor)}")
    print(f"Vendor From Software : {id(antivirus.vendor)}")

    del vendor

    print("\nAfter deleting vendor variable:")

    laptop.show_vendor()
    antivirus.show_vendor()
    

main()
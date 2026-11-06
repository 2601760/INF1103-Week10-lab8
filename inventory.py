from abc import ABC, abstractmethod


class Vendor:

    def __init__(
        self,
        vendor_id: str,
        company_name: str,
        email_address: str
    ) -> None:

        self.vendor_id: str = vendor_id
        self.company_name: str = company_name
        self.email_address: str = email_address


class Item(ABC):

    def __init__(
        self,
        item_id: str,
        item_name: str,
        unit_price: float,
        quantity_available: int,
        vendor: Vendor
    ) -> None:

        self.item_id: str = item_id
        self.item_name: str = item_name
        self.unit_price: float = unit_price
        self.quantity_available: int = quantity_available
        self.vendor: Vendor = vendor

    def get_item_id(self) -> str:
        return self.item_id

    def get_item_name(self) -> str:
        return self.item_name

    def get_unit_price(self) -> float:
        return self.unit_price

    def modify_quantity(
        self,
        amount: int
    ) -> bool:

        if self.quantity_available + amount >= 0:
            self.quantity_available += amount
            return True

        return False

    @abstractmethod
    def show_details(self) -> None:
        pass

    @abstractmethod
    def delivery_details(self) -> str:
        pass


class HardwareItem(Item):

    def __init__(
        self,
        item_id: str,
        item_name: str,
        unit_price: float,
        quantity_available: int,
        mass: float,
        vendor: Vendor
    ) -> None:

        super().__init__(
            item_id,
            item_name,
            unit_price,
            quantity_available,
            vendor
        )

        self.mass: float = mass

    def show_details(self) -> None:

        print(f"\nItem ID: {self.item_id}")
        print(f"Name: {self.item_name}")
        print(f"Price: ${self.unit_price:.2f}")
        print(f"Stock: {self.quantity_available}")
        print(f"Mass: {self.mass} kg")

    def delivery_details(self) -> str:
        return "This item requires physical delivery."


class SoftwareItem(Item):

    def __init__(
        self,
        item_id: str,
        item_name: str,
        unit_price: float,
        quantity_available: int,
        file_size: float,
        vendor: Vendor
    ) -> None:

        super().__init__(
            item_id,
            item_name,
            unit_price,
            quantity_available,
            vendor
        )

        self.file_size: float = file_size

    def show_details(self) -> None:

        print(f"\nItem ID: {self.item_id}")
        print(f"Name: {self.item_name}")
        print(f"Price: ${self.unit_price:.2f}")
        print(f"Stock: {self.quantity_available}")
        print(f"File Size: {self.file_size} MB")

    def delivery_details(self) -> str:
        return "This item is delivered digitally."


class Inventory:

    def __init__(
        self,
        inventory_name: str
    ) -> None:

        self.inventory_name: str = inventory_name
        self.products: list[Item] = []

    def add_product(
        self,
        product: Item
    ) -> None:

        self.products.append(product)

    def display_all_products(self) -> None:

        print(f"\n{self.inventory_name}")

        for product in self.products:

            product.show_details()
            print(product.delivery_details())
            print("-" * 30)


def show_item_details(
    item: Item
) -> None:

    item.show_details()
    print(item.delivery_details())


def main() -> None:

    vendor = Vendor(
        "VEN001",
        "NextGen Solutions",
        "support@nextgen.com"
    )

    laptop = HardwareItem(
        "H001",
        "Gaming Laptop",
        1999.99,
        10,
        2.5,
        vendor
    )

    antivirus = SoftwareItem(
        "S001",
        "Antivirus Pro",
        49.99,
        100,
        500,
        vendor
    )

    print("=== POLYMORPHISM TEST ===")

    print(
        "\nPrediction:"
        "\nHardwareItem -> This item requires physical delivery."
        "\nSoftwareItem -> This item is delivered digitally."
    )

    inventory = Inventory(
        "Main Inventory"
    )

    inventory.add_product(
        laptop
    )

    inventory.add_product(
        antivirus
    )

    print(
        "\nDisplaying products through "
        "the Item collection:"
    )

    inventory.display_all_products()

    print(
        "\nTesting through "
        "show_item_details(Item):"
    )

    show_item_details(
        laptop
    )

    show_item_details(
        antivirus
    )


main()
from abc import ABC, abstractmethod


class Shippable(ABC):

    @abstractmethod
    def shipping_fee(self) -> float:
        pass


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

    def show_details(self) -> None:

        print(f"Vendor ID: {self.vendor_id}")
        print(f"Company Name: {self.company_name}")
        print(f"Email Address: {self.email_address}")


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

    def get_quantity(self) -> int:
        return self.quantity_available

    def modify_quantity(
        self,
        amount: int
    ) -> bool:

        if self.quantity_available + amount >= 0:
            self.quantity_available += amount
            return True

        return False

    def show_vendor(self) -> None:
        self.vendor.show_details()

    @abstractmethod
    def delivery_details(self) -> str:
        pass

    @abstractmethod
    def show_details(self) -> None:
        pass


class HardwareItem(Item, Shippable):

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

    def shipping_fee(self) -> float:
        return self.mass * 5

    def delivery_details(self) -> str:
        return "Physical delivery required."

    def show_details(self) -> None:

        print(f"\nID: {self.item_id}")
        print(f"Name: {self.item_name}")
        print(f"Price: ${self.unit_price:.2f}")
        print(f"Quantity: {self.quantity_available}")
        print(f"Mass: {self.mass} kg")


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

    def delivery_details(self) -> str:
        return "Delivered digitally."

    def show_details(self) -> None:

        print(f"\nID: {self.item_id}")
        print(f"Name: {self.item_name}")
        print(f"Price: ${self.unit_price:.2f}")
        print(f"Quantity: {self.quantity_available}")
        print(f"File Size: {self.file_size} MB")


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

    def remove_product(
        self,
        product_id: str
    ) -> bool:

        for product in self.products:

            if product.get_item_id() == product_id:
                self.products.remove(product)
                return True

        return False

    def find_product(
        self,
        product_id: str
    ) -> Item | None:

        for product in self.products:

            if product.get_item_id() == product_id:
                return product

        return None

    def display_all_products(self) -> None:

        print(f"\n{self.inventory_name}")

        for product in self.products:
            product.show_details()
            print(product.delivery_details())


class OrderLine:

    def __init__(
        self,
        product: Item,
        quantity: int
    ) -> None:

        self.product: Item = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:

        return (
            self.product.get_unit_price()
            * self.quantity
        )


class Order:

    def __init__(
        self,
        order_id: str
    ) -> None:

        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(
        self,
        product: Item,
        quantity: int
    ) -> None:

        order_line = OrderLine(
            product,
            quantity
        )

        self.order_lines.append(order_line)

    def remove_order_line(
        self,
        product_id: str
    ) -> bool:

        for line in self.order_lines:

            if (
                line.product.get_item_id()
                == product_id
            ):
                self.order_lines.remove(line)
                return True

        return False

    def calculate_total(self) -> float:

        total: float = 0

        for line in self.order_lines:
            total += line.calculate_subtotal()

        return total

    def display_order(self) -> None:

        print(f"\nOrder ID: {self.order_id}")

        for line in self.order_lines:

            print(
                f"{line.product.get_item_name()} "
                f"x {line.quantity}"
            )

            print(
                f"Subtotal: "
                f"${line.calculate_subtotal():.2f}"
            )

        print(
            f"Total: "
            f"${self.calculate_total():.2f}"
        )


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

    print("\n=== ASSOCIATION TEST ===")

    laptop.show_vendor()
    antivirus.show_vendor()

    del vendor

    print("\nVendor still accessible through items:")

    laptop.show_vendor()
    antivirus.show_vendor()

    print("\n=== AGGREGATION TEST ===")

    inventory_a = Inventory(
        "Inventory A"
    )

    inventory_b = Inventory(
        "Inventory B"
    )

    inventory_a.add_product(
        laptop
    )

    inventory_a.display_all_products()

    inventory_a.remove_product(
        "H001"
    )

    print(
        "\nProduct still exists "
        "after removal:"
    )

    laptop.show_details()

    inventory_b.add_product(
        laptop
    )

    inventory_b.display_all_products()

    print("\n=== COMPOSITION TEST ===")

    order_1 = Order("ORD001")

    order_1.add_order_line(
        laptop,
        2
    )

    order_1.add_order_line(
        antivirus,
        3
    )

    order_1.display_order()

    order_2 = Order("ORD002")

    order_2.add_order_line(
        laptop,
        1
    )

    order_2.display_order()

    print(
        "\nSame Product Object:"
    )

    print(
        order_1.order_lines[0].product
        is order_2.order_lines[0].product
    )

    print(
        "\nSame OrderLine Object:"
    )

    print(
        order_1.order_lines[0]
        is order_2.order_lines[0]
    )

    print("\n=== LSP TEST ===")

    show_item_details(
        laptop
    )

    show_item_details(
        antivirus
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

    inventory.display_all_products()


main()
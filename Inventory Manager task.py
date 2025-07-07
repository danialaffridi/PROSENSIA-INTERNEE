import random

# 🧱 Base Product Class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} → Qty: {self.quantity}, Value: {self.total_value():.2f}"

# 🧊 Subclass for Perishable Items
class PerishableProduct(Product):
    def __init__(self, name, price, quantity, expiry_days):
        super().__init__(name, price, quantity)
        self.expiry_days = expiry_days

    def total_value(self):
        base_value = super().total_value()
        if self.expiry_days < 5:
            return base_value * 0.8  # 20% discount
        return base_value

# 📦 Inventory Manager
class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_inventory(self):
        print("📦 Inventory:")
        for idx, p in enumerate(self.products, start=1):
            print(f"{idx}. {p}")

    def search_by_name(self, term):
        print(f"🔍 Search '{term}':")
        matches = list(filter(lambda p: term.lower() in p.name.lower(), self.products))
        for item in matches:
            print(item)

    def restock_all(self):
        for product in self.products:
            restock_amount = random.randint(5, 20)
            product.quantity += restock_amount

    def export_summary(self, filename="inventory_report.txt"):
        with open(filename, "w") as f:
            lines = [
                f"{p.name}: Quantity={p.quantity}, Value={p.total_value():.2f}"
                for p in self.products
            ]
            f.write("\n".join(lines))
        print(f"✅ Report exported to {filename}")

# 🚀 Test Code
if __name__ == "__main__":
    manager = InventoryManager()

    # Add Products
    manager.add_product(Product("Apple", 5.0, 10))
    manager.add_product(PerishableProduct("Milk", 4.0, 5, expiry_days=3))
    manager.add_product(PerishableProduct("Yogurt", 3.0, 7, expiry_days=6))

    # List Inventory
    manager.list_inventory()

    # Search Product
    manager.search_by_name("milk")

    # Restock All
    print("\n🔄 Restocking...\n")
    manager.restock_all()
    manager.list_inventory()

    # Export Inventory Report
    manager.export_summary()

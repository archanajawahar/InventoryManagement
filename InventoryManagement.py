class InventoryManagement:

    def __init__(self):
        # Three warehouses
        self.warehouses = {
            "A": {},
            "B": {},
            "C": {}
        }

        self.reorder_threshold = 5

    # Add product
    def add_product(self, warehouse, product, quantity):

        if warehouse not in self.warehouses:
            return "Invalid warehouse"

        if quantity <= 0:
            return "Invalid quantity"

        if product in self.warehouses[warehouse]:
            self.warehouses[warehouse][product] += quantity
        else:
            self.warehouses[warehouse][product] = quantity

        return "Product added successfully"

    # Remove product
    def remove_product(self, warehouse, product, quantity):

        if warehouse not in self.warehouses:
            return "Invalid warehouse"

        if product not in self.warehouses[warehouse]:
            return "Invalid product"

        if quantity <= 0:
            return "Invalid quantity"

        if quantity > self.warehouses[warehouse][product]:
            return "Insufficient inventory"

        self.warehouses[warehouse][product] -= quantity

        return "Product removed successfully"

    # Transfer stock
    def transfer_stock(self, source, destination, product, quantity):

        if source not in self.warehouses or destination not in self.warehouses:
            return "Invalid warehouse"

        if product not in self.warehouses[source]:
            return "Invalid product"

        if quantity <= 0:
            return "Invalid quantity"

        if quantity > self.warehouses[source][product]:
            return "Insufficient inventory"

        self.warehouses[source][product] -= quantity

        if product in self.warehouses[destination]:
            self.warehouses[destination][product] += quantity
        else:
            self.warehouses[destination][product] = quantity

        return "Stock transferred successfully"

    # Reorder
    def reorder(self, warehouse, product):

        if warehouse not in self.warehouses:
            return "Invalid warehouse"

        if product not in self.warehouses[warehouse]:
            return "Invalid product"

        if self.warehouses[warehouse][product] <= self.reorder_threshold:
            self.warehouses[warehouse][product] += 10
            return "Stock reordered successfully"

        return "Reorder not required"

    # Low-stock detection
    def low_stock(self, warehouse, product):

        if warehouse not in self.warehouses:
            return "Invalid warehouse"

        if product not in self.warehouses[warehouse]:
            return "Invalid product"

        if self.warehouses[warehouse][product] <= self.reorder_threshold:
            return "Low stock"

        return "Stock level normal"

    # Automatically select warehouse
    def select_warehouse(self, product, quantity):

        for warehouse in ["A", "B", "C"]:
            if product in self.warehouses[warehouse]:
                if self.warehouses[warehouse][product] >= quantity:
                    return warehouse

        return "No warehouse has sufficient stock"

    # Display inventory
    def display_inventory(self):

        for warehouse in self.warehouses:
            print("\nWarehouse", warehouse)

            if not self.warehouses[warehouse]:
                print("No products")
            else:
                for product, quantity in self.warehouses[warehouse].items():
                    print(product, ":", quantity)


# ---------------- MAIN PROGRAM ----------------

inventory = InventoryManagement()

# Add products
print(inventory.add_product("A", "Laptop", 20))
print(inventory.add_product("B", "Laptop", 10))
print(inventory.add_product("C", "Phone", 15))

# Remove product
print(inventory.remove_product("A", "Laptop", 2))

# Transfer stock
print(inventory.transfer_stock("A", "Laptop", "B", 5))

# Low-stock detection
print(inventory.low_stock("B", "Laptop"))

# Reorder
print(inventory.reorder("B", "Laptop"))

# Automatic warehouse selection
warehouse = inventory.select_warehouse("Laptop", 10)
print("Selected Warehouse:", warehouse)

# Display inventory
print("\nInventory:")
inventory.display_inventory()

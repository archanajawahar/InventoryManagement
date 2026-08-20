from InventoryManagement import InventoryManagement


print("===== INVENTORY MANAGEMENT QA =====")

inventory = InventoryManagement()

# Add test data
inventory.add_product("A", "Laptop", 20)
inventory.add_product("B", "Laptop", 10)
inventory.add_product("C", "Phone", 15)


# 1. Stock availability
print("\n1. Stock Availability")
warehouse = inventory.select_warehouse("Laptop", 5)
print("Selected Warehouse:", warehouse)


# 2. Insufficient inventory
print("\n2. Insufficient Inventory")
print(inventory.remove_product("A", "Laptop", 100))


# 3. Warehouse transfer
print("\n3. Warehouse Transfer")
print(inventory.transfer_stock("A", "Laptop", "B", 5))


# 4. Concurrent orders
print("\n4. Concurrent Orders")
print("Multiple orders tested on the same inventory.")
print(inventory.remove_product("B", "Laptop", 2))
print(inventory.remove_product("B", "Laptop", 2))


# 5. Reorder threshold
print("\n5. Reorder Threshold")

inventory.add_product("A", "Mouse", 5)

print("Stock Status:",
      inventory.low_stock("A", "Mouse"))

print("Reorder:",
      inventory.reorder("A", "Mouse"))


# 6. Invalid product
print("\n6. Invalid Product")
print(inventory.remove_product("A", "Keyboard", 2))


# 7. Negative inventory
print("\n7. Negative Inventory")
print(inventory.remove_product("A", "Laptop", 1000))


# 8. Multiple warehouses
print("\n8. Multiple Warehouses")

print("Warehouse A:", inventory.warehouses["A"])
print("Warehouse B:", inventory.warehouses["B"])
print("Warehouse C:", inventory.warehouses["C"])


print("\n===== QA COMPLETED =====")

# link to project: https://github.com/ZenithMelody/inf1103-lab4

inventory = 0
failed_Enteries = 0
total_Tax = 0.0
orders = []

def load_inventory():
    global orders
    try:
        # make txt if empty
        with open("orders.txt", "a+") as f:
            f.seek(0)
            orders = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        orders = []

def save_inventory():
    with open("orders.txt", "w") as f:
        for order in orders:
            f.write(order + "\n")

# report summary
def generate_report(inventory, failed_Enteries, total_Tax):
    print("\nReport Summary")
    print(f"Total Units Processed: {inventory}")
    print(f"Total amount of Tax: {total_Tax:.2f}")
    print(f"Number of Failed/Rejected Entries: {failed_Enteries}")

load_inventory()

print("Current Orders:\n")
for order in orders:
    print(order)
print()

# user input
product_name = input("Enter Product Name: ")
quantity = input("Enter Quantity: ")

# incremental order ID 
next_id = 1001 if not orders else int(orders[-1].split(",")[0].strip()) + 1
new_order = f"{next_id}, {product_name}, {quantity}"

orders.append(new_order)
save_inventory()

print("\nNew Order Added:")
print(f"{next_id},{product_name},{quantity}\n")
print("Order successfully saved to orders.txt")
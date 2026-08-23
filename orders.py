import json

ORDERS_FILE = "orders.json"

def load_orders(filename):
    with open(filename, "r") as f:
        return json.load(f)

def total_revenue(orders):
    total = 0
    for order in orders:
        total += order["amount"]
    return total

def main():
    try:
        orders = load_orders(ORDERS_FILE)
    except FileNotFoundError:
        print(f"{ORDERS_FILE} not found.")
        return
    revenue = total_revenue(orders)
    print(f"Total revenue: ${revenue:.2f}")

if __name__ == "__main__":
    main()

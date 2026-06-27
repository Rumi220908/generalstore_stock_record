class Transaction:
    def __init__(self, item, date, action, quantity, price):
        self.item = item.title()
        self.date = date
        self.action = action
        self.quantity = quantity
        self.price = price
        self.total = quantity * price


transactions = []
stock = {}


def show_stock():
    print("\n===== CURRENT STOCK =====")
    with open("store_transactions.txt", "r") as file:
        print(file.read())



def save_transaction(t):
    transactions.append(t)

    with open("store_transactions.txt", "a") as file:
        file.write(
            f"{t.date:<15}"
            f"{t.item:<20}"
            f"{t.action:<12}"
            f"{t.quantity:<10}"
            f"{t.price:<10}"
            f"{t.total}\n"
        )


def add_stock(t):
    stock[t.item] = stock.get(t.item, 0) + t.quantity


def sell_stock(t):
    transactions.append(t)

    with open("store_transactions.txt", "a") as file:
        file.write(
            f"{t.date:<15}"
            f"{t.item:<20}"
            f"{t.action:<12}"
            f"{t.quantity:<10}"
            f"{t.price:<10}"
            f"{t.total}\n"
        )


def create_transaction(action):

    item = input("\nProduct name: ").title()
    date = input("Date (DD/MM/YYYY): ")

    try:
        quantity = int(input("Quantity: "))
        price = float(input("Price per item: ₹"))

    except ValueError:
        print("Enter valid numbers.")
        return

    t = Transaction(item, date, action, quantity, price)

    print("\n----- CHECK DETAILS -----")
    print("Product :", t.item)
    print("Date    :", t.date)
    print("Type    :", t.action)
    print("Qty     :", t.quantity)
    print("Price   : ₹", t.price)
    print("Total   : ₹", t.total)

    confirm = input("\nConfirm (yes/no): ").lower()

    if confirm != "yes":
        print("Transaction cancelled.")
        return

    if action == "Purchase":
        add_stock(t)

    else:
        if not sell_stock(t):
            return

    save_transaction(t)

    print("\nTransaction saved successfully.")



print("=== GENERAL STORE MANAGEMENT ===")

while True:

    print("""
1. Buy / Register Stock
2. Sell Product
3. View Stock
4. Exit
""")

    choice = input("Choose: ")

    if choice == "1":
        create_transaction("Purchase")

    elif choice == "2":
        create_transaction("Sale")

    elif choice == "3":
        show_stock()

    elif choice == "4":
        break

    else:
        print("Invalid choice.")


print("\n===== TRANSACTION HISTORY IN THIS SESSION =====")

if len(transactions) == 0:
    print("No transactions found in this session.")

else:
    for t in transactions:
        print(
            f"{t.date:<15}"
            f"{t.item:<15}"
            f"{t.action:<12}"
            f"{t.quantity:<8}"
            f"₹{t.total}"
        )

print("\nAll data saved in store_transactions.txt")
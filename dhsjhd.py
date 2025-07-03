import datetime

# Initial product data
products = {
    1: {"title": "1984", "author": "George Orwell", "category": "Novel", "price": 15.0, "stock": 10},
    2: {"title": "Clean Code", "author": "Robert C. Martin", "category": "Programming", "price": 30.0, "stock": 5},
    3: {"title": "The Alchemist", "author": "Paulo Coelho", "category": "Fiction", "price": 12.0, "stock": 7},
    4: {"title": "Python Crash Course", "author": "Eric Matthes", "category": "Programming", "price": 25.0, "stock": 4},
    5: {"title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy", "price": 20.0, "stock": 8}
}

sales = []

# --- Inventory Management ---
def add_product():
    try:
        product_id = max(products.keys()) + 1
        title = input("Enter title: ")
        author = input("Enter author: ")
        category = input("Enter category: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        products[product_id] = {
            "title": title, "author": author,
            "category": category, "price": price, "stock": stock
        }
        print("✅ Product successfully added.")
    except Exception as e:
        print("❌ Error:", e)

# --- Sales Registration ---
def register_sale():
    try:
        client = input("Enter client name: ")
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
        discount = float(input("Enter discount (0 if none): "))

        if product_id not in products:
            print("❌ Product not found.")
            return

        if quantity > products[product_id]["stock"]:
            print("❌ Not enough stock available.")
            return

        # Update stock
        products[product_id]["stock"] -= quantity

        sale = {
            "client": client,
            "product_id": product_id,
            "quantity": quantity,
            "discount": discount,
            "date": datetime.date.today()
        }
        sales.append(sale)
        print("✅ Sale successfully registered.")
    except Exception as e:
        print("❌ Error:", e)

# --- Reports ---
def report_top_3_products():
    from collections import Counter
    counter = Counter()
    for sale in sales:
        counter[sale["product_id"]] += sale["quantity"]
    top = counter.most_common(3)
    print("\nTop 3 Best-Selling Products:")
    for pid, qty in top:
        print(f"{products[pid]['title']} - Sold: {qty}")

def report_sales_by_author():
    author_sales = {}
    for sale in sales:
        author = products[sale["product_id"]]["author"]
        author_sales[author] = author_sales.get(author, 0) + sale["quantity"]
    print("\nSales Grouped by Author:")
    for author, qty in author_sales.items():
        print(f"{author}: {qty} sold")

def report_revenue():
    gross = sum(products[s["product_id"]]["price"] * s["quantity"] for s in sales)
    net = sum((products[s["product_id"]]["price"] - s["discount"]) * s["quantity"] for s in sales)
    print(f"\n💰 Gross Income: ${gross:.2f}")
    print(f"💰 Net Income (after discounts): ${net:.2f}")

# --- Menu ---
def main_menu():
    while True:
        print("\n📚 Inventory and Sales Management System")
        print("1. Add Product")
        print("2. Register Sale")
        print("3. Show Top 3 Best-Selling Products")
        print("4. Show Sales by Author")
        print("5. Show Revenue Report")
        print("6. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            add_product()
        elif choice == '2':
            register_sale()
        elif choice == '3':
            report_top_3_products()
        elif choice == '4':
            report_sales_by_author()
        elif choice == '5':
            report_revenue()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()

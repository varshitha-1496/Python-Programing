portfolio = {}

def add_stock():
    symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
    shares = int(input(f"How many shares of {symbol}? "))
    price = float(input(f"Current price per share of {symbol}? ₹ "))
    
    portfolio[symbol] = {
        "shares": shares,
        "price": price
    }
    print(f"✅ Added {shares} shares of {symbol} at ₹{price} each.")

def view_portfolio():
    if not portfolio:
        print("Your portfolio is empty.")
        return

    print("\n📊 Your Portfolio:")
    total_value = 0

    for symbol, info in portfolio.items():
        value = info["shares"] * info["price"]
        total_value += value
        print(f"{symbol}: {info['shares']} shares × ₹{info['price']} = ₹{value:.2f}")
    
    print(f"\n💰 Total Portfolio Value: ₹{total_value:.2f}")

def show_menu():
    print("\n--- Stock Portfolio Tracker ---")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Exit")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_stock()
    elif choice == '2':
        view_portfolio()
    elif choice == '3':
        print("Exiting... Bye!")
        break
    else:
        print("Invalid option. Please choose 1, 2, or 3.")

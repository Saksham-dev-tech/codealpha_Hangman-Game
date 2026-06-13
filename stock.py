# 1. Hardcoded dictionary defining stock prices
STOCK_PRICES = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "MSFT": 320.0,
    "GOOG": 140.0,
    "AMZN": 130.0
}

def main():
    print("--- Welcome to the Simple Stock Tracker ---")
    print("Available stocks to track:", ", ".join(STOCK_PRICES.keys()))

    total_investment = 0.0
    portfolio = [] # List to keep track of what the user adds

    # Loop to allow multiple inputs
    while True:
        # User input for stock name
        stock_name = input("\nEnter stock name (or type 'done' to finish): ").strip().upper()

        if stock_name == 'DONE':
            break

        if stock_name not in STOCK_PRICES:
            print(f"Error: We don't have price data for {stock_name}. Try one from the list.")
            continue

        # User input for quantity
        quantity_str = input(f"How many shares of {stock_name} do you own? ")

        # Simple check to make sure the user typed a number
        if not quantity_str.replace('.', '', 1).isdigit():
            print("Invalid input. Please enter a valid number for the quantity.")
            continue

        quantity = float(quantity_str)

        # Basic arithmetic to calculate value
        price = STOCK_PRICES[stock_name]
        stock_value = price * quantity
        total_investment += stock_value

        # Format the entry and add it to our portfolio list
        entry = f"{stock_name}: {quantity} shares @ ${price} = ${stock_value:.2f}"
        portfolio.append(entry)

        print(f"Added! Running Total Investment: ${total_investment:.2f}")

    # Display final total investment value
    print("\n" + "="*30)
    print("      PORTFOLIO SUMMARY      ")
    print("="*30)
    for item in portfolio:
        print(item)
    print("-" * 30)
    print(f"TOTAL VALUE: ${total_investment:.2f}")
    print("="*30)

    # Optional file handling: Saving to a .txt file
    save_choice = input("\nWould you like to save this summary to a text file? (y/n): ").strip().lower()
    if save_choice == 'y':
        # Open (or create) the file in 'write' mode
        with open("investment_summary.txt", "w") as file:
            file.write("--- Portfolio Summary ---\n")
            for item in portfolio:
                file.write(item + "\n")
            file.write(f"\nTOTAL VALUE: ${total_investment:.2f}\n")
        print("Success! Your summary has been saved to 'investment_summary.txt'.")

if __name__ == "__main__":
    main()
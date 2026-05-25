# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 150
}
total_investment = 0
print("Welcome to Stock Portfolio Tracker")
print("----------------------------------")
# Taking user input
while True:
    stock_name = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print(f"Added {quantity} shares of {stock_name}")
        print(f"Investment Value: ${investment}\n")
    else:
        print("Stock not found in database.\n")
# Display total investment
print("----------------------------------")
print(f"Total Investment Value: ${total_investment}")
# Save result to file
save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    file = open("portfolio_result.txt", "w")
    file.write(f"Total Investment Value: ${total_investment}")
    file.close()
    print("Result saved to portfolio_result.txt")
print("Thank you for using Stock Portfolio Tracker!")
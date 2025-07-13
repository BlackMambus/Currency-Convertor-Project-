import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "result" not in data:
        return "Error: Unable to fetch exchange rate."

    converted_amount = data["result"]
    rate = data["info"]["rate"]
    return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency} (Rate: {rate:.4f})"

def main():
    print("💱 Currency Converter")
    while True:
        from_currency = input("From currency (e.g., USD): ").upper()
        to_currency = input("To currency (e.g., INR): ").upper()
        try:
            amount = float(input("Amount to convert: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        result = convert_currency(amount, from_currency, to_currency)
        print(result)

        again = input("Convert another? (y/n): ").lower()
        if again != 'y':
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    main()





import csv

def load_exchange_rates(filename):
    with open(filename, mode='r', encoding='ISO-8859-1') as file:
        return {row['code'].strip(): float(row['rate'].strip()) for row in csv.DictReader(file, delimiter=',')}

def convert_currency(usd, target_currency, rates):
    return usd * rates.get(target_currency, None)

def main():
    file_path = 'Activity_4B\currency.csv'
    rates = load_exchange_rates(file_path)
    try:
        usd = float(input("How much dollar do you have? "))
        target_currency = input("What currency you want to have? ").upper()
        converted_amount = convert_currency(usd, target_currency, rates)
        
        print("-------------------------------")
        print(f"Dollar: {usd} USD")
        print(f"{target_currency}: {converted_amount:.2f}" if converted_amount else "Invalid currency.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

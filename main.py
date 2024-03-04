from ExchangeRateFetcher import ExchangeRateFetcher as erf
from CurrencyGoldExchanger import CurrencyGoldExchanger as cge

def print_error_message(error_message):
    """Prints an error message.

    Args:
        error_message (str): The error message to be printed.
    """
    print(f"An error occurred: {error_message}")

def print_exchange_info(amount, currency1, amount2, currency2):
    """Prints the exchange information.

    Args:
        amount (float): The amount of currency1.
        currency1 (str): The name of the first currency.
        amount2 (float): The amount of currency2.
        currency2 (str): The name of the second currency.
    """
    print(f"With {amount} {currency1.upper()}, you could buy {amount2} {currency2.upper()}")

def process_exchange(amount, currency1, amount2, currency2):
    """Processes the exchange and prints the exchange information.

    Args:
        amount (float): The amount of currency1.
        currency1 (str): The name of the first currency.
        amount2 (float): The amount of currency2.
        currency2 (str): The name of the second currency.
    """
    if isinstance(amount2, str):
        print_error_message(amount2)
    else:
        print_exchange_info(amount, currency1, amount2, currency2)

def main():
    """Demonstrates the capabilities of the ExchangeRateFetcher and CurrencyGoldExchanger classes."""
    fetcher = erf()
    exchanger = cge()
    
    currencies = ['usd']
    pln_amount = 15340000
    foreign_currency_amount = 90232
    
    for currency in currencies:
        print(f"\nProcessing for currency: {currency.upper()}")
        
        # Fetch the average exchange rate of foreign currency
        avg_exchange_rate = fetcher.get_avg_exchange_rate(currency)
        if isinstance(avg_exchange_rate, str):
            print_error_message(avg_exchange_rate)
        else:
            print(f"Current average exchange rate for {currency.upper()}: {avg_exchange_rate}")
        
        # Calculate how much foreign currency could be bought with the PLN amount
        foreign_amount = exchanger.pln_to_curr(pln_amount, currency)
        process_exchange(pln_amount, "pln", foreign_amount, currency)
        
        # Calculate how much gold (in kg) could be bought with the PLN amount
        gold_in_kg = exchanger.pln_to_gold(pln_amount)
        process_exchange(pln_amount, "pln", gold_in_kg, "kg of gold")

        # Calculate how much PLN could be bought with the foreign currency amount
        pln = exchanger.curr_to_pln(foreign_currency_amount, currency)
        process_exchange(foreign_currency_amount, currency, pln, "pln")

        # Calculate how much gold (in kg) could be bought with the foreign currency amount
        gold_in_kg = exchanger.curr_to_gold(foreign_currency_amount, currency)
        process_exchange(foreign_currency_amount, currency, gold_in_kg, "kg of gold")

if __name__ == "__main__":
    main()

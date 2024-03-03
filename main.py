from ExchangeRateFetcher import ExchangeRateFetcher as erf
from CurrencyGoldExchanger import CurrencyGoldExchanger as cge

def main():
    """Demonstrates the capabilities of the ExchangeRateFetcher and CurrencyGoldExchanger classes."""
    fetcher = erf()
    exchanger = cge()
    
    currencies = ['usd']
    pln_amount = 1534
    foreign_currency_amount = 902
    
    for currency in currencies:
        print(f"\nProcessing for currency: {currency.upper()}")
        
        # Fetch the average exchange rate of foreign currency
        avg_exchange_rate = fetcher.get_avg_exchange_rate(currency)
        print(f"Current average exchange rate for {currency.upper()}: {avg_exchange_rate}")
        
        # Calculate how much foreign currency could be bought with the PLN amount
        foreign_currency = exchanger.pln_to_curr(pln_amount, currency)
        print(f"With {pln_amount} PLN, you could buy {foreign_currency} {currency.upper()}")
        
        # Calculate how much gold (in kg) could be bought with the PLN amount
        gold_in_kg = exchanger.pln_to_gold(pln_amount)
        print(f"With {pln_amount} PLN, you could buy {gold_in_kg} kg of GOLD")
        
        # Calculate how much PLN could be bought with the foreign currency amount
        pln = exchanger.curr_to_pln(foreign_currency_amount, currency)
        print(f"With {foreign_currency_amount} {currency.upper()}, you could buy {pln} PLN")
        
        # Calculate how much gold (in kg) could be bought with the foreign currency amount
        gold_in_kg = exchanger.curr_to_gold(foreign_currency_amount, currency)
        print(f"With {foreign_currency_amount} {currency.upper()}, you could buy {gold_in_kg} kg of GOLD")

if __name__ == "__main__":
    main()

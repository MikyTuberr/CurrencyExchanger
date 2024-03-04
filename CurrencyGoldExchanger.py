from ExchangeRateFetcher import ExchangeRateFetcher as erf

class CurrencyGoldExchanger:
    """A class to exchange given currency, using the NBP API."""
    
    def __init__(self):
        """
        Initializes the CurrencyGoldExchanger with a fetcher.
        
        Args:
            fetcher (ExchangeRateFetcher): An instance of ExchangeRateFetcher to fetch exchange rates and gold prices.
        """
        self.fetcher = erf()

    def pln_to_curr(self, pln, currency):
        """
        Exchanges PLN to the given currency using the current exchange rate.
        
        Args:
            pln (float): The amount in PLN to exchange.
            currency (str): The currency code to exchange to.

        Returns:
            float or str: The equivalent amount in the given currency if successful, 
                          otherwise an error message from the fetcher.
        """
        rate = self.fetcher.get_buying_rate(currency)
        if isinstance(rate, str):
            return rate  # This is an error message from get_buying_rate
        return pln / rate
    

    def pln_to_gold(self, pln):
        """
        Calculates how many kilograms of gold can be bought for the given amount in PLN.
        
        Args:
            pln (float): The amount in PLN to exchange.

        Returns:
            float or str: The equivalent amount in kilograms of gold if successful, 
                          otherwise an error message from the fetcher.
        """
        rate = self.fetcher.get_gold_rate()
        if isinstance(rate, str):
            return rate  # This is an error message from get_gold_rate
        return pln / rate / 1000
    
    
    def curr_to_pln(self, amount, currency):
        """
        Exchanges given currency to PLN using the current exchange rate.
        
        Args:
            amount (float): The amount in given currency to exchange.
            currency (str): The currency code to exchange to.

        Returns:
            float or str: The equivalent amount in PLN if successful, 
                          otherwise an error message from the fetcher.
        """
        rate = self.fetcher.get_selling_rate(currency)
        if isinstance(rate, str):
            return rate  # This is an error message from get_selling_rate
        return amount * rate

    def curr_to_gold(self, amount, currency):
        """
        Calculates how many kilograms of gold can be bought for given amount in the given currency.
        
        Args:
            amount (float): The amount in given currency to exchange.
            currency (str): The currency code to exchange to.

        Returns:
            float or str: The equivalent amount in kilograms of gold if successful, 
                          otherwise an error message from the fetcher.
        """
        pln = self.curr_to_pln(amount, currency)
        if isinstance(pln, str):
            return pln  # This is an error message from curr_to_pln
        return self.pln_to_gold(pln)
    

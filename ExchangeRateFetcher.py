import requests

class ExchangeRateFetcher:
    """A class to fetch exchange rates and gold prices from the NBP API."""
    
    def __init__(self) -> None:
        """Initializes the API URL and format."""
        self._API_URL = 'http://api.nbp.pl/api'
        self._FORMAT_JSON = '/?format=json'
        
    def _fetch_data(self, endpoint: str, currency: str = None) -> dict | str:
        """
        Helper method to fetch data from the NBP API.
        
        Args:
            endpoint (str): The endpoint to fetch data from.
            currency (str, optional): The currency code to get the rate of.

        Returns:
            dict or str: The JSON response if successful, otherwise an error message.
        """
        url = f'{self._API_URL}/{endpoint}'
        if currency:
            url += f'/{currency}'
        url += f'/today/{self._FORMAT_JSON}'
        
        response = requests.get(url)
        if response.status_code != 200:
            url = url.replace('/today', '')
            response = requests.get(url)
            if response.status_code != 200:
                return f"Error {response.status_code}: Failed to fetch data"
            
        return response.json()
    
    def get_avg_exchange_rate(self, currency: str) -> float | str:
        """
        Fetches the current average exchange rate for the given currency from the NBP API.
        
        Args:
            currency (str): The currency code to get the exchange rate of.

        Returns:
            float or str: The current average exchange rate of the currency if successful, 
                          otherwise an error message.
        """
        data = self._fetch_data('exchangerates/rates/a', currency)
        if isinstance(data, str):
            return data
        return data['rates'][0]['mid']
    
    def get_selling_rate(self, currency: str) -> float | str:
        """
        Fetches the current selling rate for the given currency from the NBP API.
        
        Args:
            currency (str): The currency code to get the selling rate of.

        Returns:
            float or str: The current selling rate of the currency if successful, 
                          otherwise an error message.
        """
        data = self._fetch_data('exchangerates/rates/c', currency)
        if isinstance(data, str):
            return data
        return data['rates'][0]['bid']
    
    def get_buying_rate(self, currency: str) -> float | str:
        """
        Fetches the current buying rate for the given currency from the NBP API.
        
        Args:
            currency (str): The currency code to get the buying rate of.

        Returns:
            float or str: The current buying rate of the currency if successful, 
                          otherwise an error message.
        """
        data = self._fetch_data('exchangerates/rates/c', currency)
        if isinstance(data, str):
            return data
        return data['rates'][0]['ask']
    
    def get_gold_rate(self) -> float | str:
        """
        Fetches the current gold price from the NBP API.

        Returns:
            float or str: The current price of gold per gram in PLN if successful, 
                          otherwise an error message.
        """
        data = self._fetch_data('cenyzlota')
        if isinstance(data, str):
            return data
        return data[0]['cena']

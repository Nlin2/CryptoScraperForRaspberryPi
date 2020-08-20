import requests
import json
import time 

class BinanceAPI():
    """
    Binance API Client used to extract data and buy/sell crypto
    
    notes:
    * symbol value follows this format PRODUCTCURRENCY
        * i.e. BTCUSD means BTC value according to USD
    """
    # Initializations
    def __init__(self, API_KEY=None, API_SECRET=None):
        self.END_POINT = 'https://api.binance.us'
        self.API_KEY=API_KEY
        self.API_SECRET=API_SECRET
        self.session = self._init_session()
        
    def _init_session(self):
        session = requests.session()
        session.headers.update({'Accept': 'application/json',
                                'User-Agent': 'binance/python',
                                'X-MBX-APIKEY': self.API_KEY})
        return session
    
    # General EndPoints
    def ping(self):
        """
        Test connectivity to the Rest API.
        """
        address = '/api/v3/ping'
        resp = requests.get(self.END_POINT + address)
        return json.loads(resp.text)
    def get_server_time(self):
        """
        Test connectivity to the Rest API and get the current server time
        """
        address = '/api/v3/time'
        resp =  requests.get(self.END_POINT + address)
        return json.loads(resp.text)
    def get_exchange_info(self):
        """
        Current exchange trading rules and symbol information
        
        Rate limits:
        1200 requests per minute
        10 orders per second
        100,000 orders per 24hrs
        """
        address = '/api/v3/exchangeInfo'
        resp = requests.get(self.END_POINT + address)
        return json.loads(resp.text)

    # Data Extractions
    def get_price(self, symbol):
        address = '/api/v3/ticker/bookTicker'
        resp = self.session.get(self.END_POINT + address, params={"symbol":symbol})
        timestamp = time.time()
        d = json.loads(resp.text)
        d["timestamp"] = timestamp
        return d
        
        
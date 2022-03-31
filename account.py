from ib_insync import IB
from tradingsession import TradingSession

"""
Account Class to store all of the details for the trading account, this info should be stored in a secure file and imported
and passed in via the main.py file
"""
class Account():
    def __init__(self, email, trade_capital, start_capital, port, id, exchange):
        self.email = email
        self.trade_cap = trade_capital
        self.starting_cap = start_capital 
        self.client = self._createClient()  #  Create an IB Client with ib_insync's IB Class
        self.port = port  # Trading port (usually 4001)
        self.id = id
        self.exchange = exchange
        self.startSession()

    #  Start an instance of the TradingSession class
    def startSession(self):
        self.trade_session = TradingSession(self)
    
    #  Change the email address atrributed to the account
    def changeEmail(self, email):
        self.email = email
    
    #  Change the amount of capital in the account to be used for trading
    def changeTradeCap(self, trade_cap):
        self.trade_cap = trade_cap

    #  Change (potentially create a new) client (Connection to IB)
    def changeClient(self, client):
        self.client = client

    #  Create a new client object
    def _createClient(self):
        client = IB()   
        return client

    #  Change port number for client connection
    def changePort(self, port):
        self.port = port

    #  Change the ID of the current client
    def changeID(self, id):
        self.id = id

    #  Connect the client to IB via gateway or TWS
    def connectClient(self):
        if not self.client.isConnected():
            self.client.connect('127.0.0.1', port=self.port, clientId=self.id)  # '127.0.0.1 for local network

    #  Disconnect the client from IB via gateway of TWS
    def disconnectClient(self):
        if self.client.isConnected():
            self.client.disconnect()
import json
import os
from datetime import datetime
from trading.CTradeStock import CStockData
from sender.CSender import CNotiSender

class CTradingBOT:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(CTradingBOT, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.m_AllStocks = []
        self.m_Sender = CNotiSender()

    def _readData(self):
        file_path = os.path.join(os.path.dirname(__file__), '../price.json')
        with open(file_path, 'r') as file:
            listStocks = json.load(file)
            for record in listStocks:
                stock = CStockData()
                stock.read_jsonData(record)
                self.m_AllStocks.append(stock)

    def _writeData(self):
        file_path = os.path.join(os.path.dirname(__file__), '../price.json')
        with open(file_path, 'w') as file:
            data = []
            for stock in self.m_AllStocks:
                data.append(stock.write_jsonData())
            json.dump(data, file, indent=4)

    def _queryData(self):
        status = ''
        for stock in self.m_AllStocks:
            stock.g_Frame1d(True)
            stock.queryData()
            if stock.g_Log() != '':
                status += stock.g_Log()
            #end if
            stock.updatePrice()
        #end for

        if (self.m_Sender is not None) and (status != ''):
            self.m_Sender.sendMessage(status)

    def active(self):
        self._readData()
        self._queryData()
        self._writeData()
    #end def
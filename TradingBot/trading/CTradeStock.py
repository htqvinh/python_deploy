import yfinance as yf
from trading.CTradeCondition import *

class CStockData:
    def __init__(self):
        self.m_StockId = ''
        self.m_Price = 0
        self.m_Log = ''
        self.m_Frame1d = None
        self.m_Conditions = []
    #end def

    def g_Frame1d(self, isLatest = False):
        if(isLatest):
            self.m_Frame1d = yf.Ticker(self.m_StockId).history(period="1d")
        return self.m_Frame1d

    def g_Log(self):
        return self.m_Log
    #endef
    
    def g_newPrice(self):
        if self.m_Frame1d is None:
            return float(0.0)
        return round(float(self.m_Frame1d['Close'].iloc[-1]), 2)

    def g_currPrice(self):
        return round(float(self.m_Price), 2)
    
    def updatePrice(self):
        newPrice = self.g_newPrice()
        if(newPrice != self.m_Price):
            self.m_Price = newPrice

    def queryData(self):
        self.m_Log = ''
        if self.g_Frame1d() is not None:
            logs = ''
            for cond in self.m_Conditions:
                if cond.check():
                    logs += f'{cond.g_Log()}\n'
            #end for
            if logs != '':
                self.m_Log += f'[{self.m_StockId}]\n'
                self.m_Log += logs
    #end def

    def read_jsonData(self, jsonData):
        if(jsonData is not None):
            self.m_StockId = jsonData["stockid"]
            self.m_Price = jsonData["price"]
            self.m_Conditions = [
                CCond_LessThanPrevPrice(self, 0/100),
                CCond_GreaterThanPrevPrice(self, 0/100)
            ]
        #end if
    #end def

    def write_jsonData(self):
        data = {
            "stockid" : f"{self.m_StockId}",
            "price" : f"{round(self.m_Price, 2)}"
        }
        return data
    #end def

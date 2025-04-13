from trading.CTradeStock import *

class CTradeCondition:
    
    def __init__(self, stock):
        self.m_Log = ''
        self.m_Stock = stock

    def check(self):
        return True
    
    def g_Log(self):
        return self.m_Log
    #endef
#end class

class CCond_LessThanPrevPrice(CTradeCondition):
    def __init__(self, stock, percent):
        super().__init__(stock)
        self.m_Percent = percent

    def check(self):
        oldPrice = self.m_Stock.g_currPrice()
        newPrice = self.m_Stock.g_newPrice()
        if newPrice < (oldPrice + (oldPrice * self.m_Percent)):
            percent = 0.0
            if(oldPrice > 0):
                percent = (newPrice / oldPrice)
            self.m_Log = f'-price: {newPrice} (-{round(percent, 2)}%)'
            return True
        return False
#end class


class CCond_GreaterThanPrevPrice(CTradeCondition):
    def __init__(self, stock, percent):
        super().__init__(stock)
        self.m_Percent = percent

    def check(self):
        oldPrice = self.m_Stock.g_currPrice()
        newPrice = self.m_Stock.g_newPrice()
        if newPrice > (oldPrice + (oldPrice * self.m_Percent)):
            percent = 0.0
            if(oldPrice > 0):
                percent = (newPrice / oldPrice)
            self.m_Log = f'-price: {newPrice} (+{round(percent, 2)}%)'
            return True
        return False
#end class

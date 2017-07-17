# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 11:06:01 2017

stores collated information on stocks

@author: karin
"""
from stock import Stock
from trade import Trade
import numpy as np

class StockMarket:
    stocklist={}
    def __init__(self):
        self.stocklist={'TEA':Stock('TEA','Common', 0,None,100), 'POP':Stock('POP','Common', 8,None,100) ,
        'ALE':Stock('ALE','Common', 23,None,60),'GIN':Stock('GIN','Preferred', 8,2,100) ,
        'JOE':Stock('JOE','Common', 13,None,250)} 
        
        
    def calculate_dividend_yield(self, stock, price):
        """. For a given stock,   Given any price as input, calculate the dividend yield """
        if stock.common:
            return self.stocklist[stock].get_last_dividend/price
        elif stock.preferred:
            return self.stocklist[stock].get_fixed_dividend_par_value/price
        

    def calculate_PE_Ratio(self,stock,price):
        """. For a given stock,. Given any price as input,  calculate the P/E Ratio """
        return price/self.stocklist[stock].get_dividend()

    def record_trade(self,stock,timestamp, quantity,tradetype,price):
        """Record a trade, with timestamp, quantity of shares, buy or sell indicator and traded price """
        self.stocklist[stock].add_trade(Trade(timestamp, quantity,tradetype,price))
        
        
    def calculate_volume_weighted_stock_price(self,stock):
        """iv. Calculate Volume Weighted Stock Price based on trades in past 15 minutes """
        return stock.calculate_volume_weighted_stock_price()
        
    def calculate_all_share_index(self):
        """ Calculate the GBCE All Share Index using the geometric mean of prices for all stocks"""
        for stock in self.stocklist.values():
            price_products=[t.get_price() for t in stock.get_trades() ]
            
        if len(price_products)>0:
            return np.prod(price_products)**(1.0/len(price_products))
        else:
            return 0.0
        
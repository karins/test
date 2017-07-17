# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:26:04 2017

@author: karin

Stores information on individual Stock item
"""
import numpy as np
import math
import datetime 
from datetime import timedelta 

class Stock:
    #replace with enum
    stocktypes={'Common':0,'Preferred':1}
    
    def __init__(self,stocksymbol ,stocktype,last_dividend,fixed_dividend , par_value):
        self.stocksymbol=stocksymbol
        self.stocktype=stocktype
        self.last_dividend=last_dividend
        self.fixed_dividend=fixed_dividend
        self.par_value=par_value
        self.trades=set()
        
    def get_last_dividend(self):
        return self.last_dividend
    
    def get_stocksymbol(self):
        return self.stocksymbol

    def get_stocktype(self):
        return self.stocktype
        
    def get_fixed_dividend(self):
        return self.fixed_dividend
        
    def get_par_value(self):
        return self.par_value
        
    def add_trade(self, trade):
        self.trades.add(trade)
        
    def set_trade(self, trades):
        self.trades =trades

    def get_trades(self):
        return self.trades    
    
    def calculate_volume_weighted_stock_price(self):
        """iv. Calculate Volume Weighted Stock Price based on trades in past 15 minutes """
        time_filtered_trades= [t for t in self.trades if t.timestamp< datetime.datetime.now() - datetime.timedelta(minutes = 15)]
        
        return math.fsum(t.get_price() * t.get_quantity() in time_filtered_trades)/math.fsum( t.get_quantity() in time_filtered_trades)

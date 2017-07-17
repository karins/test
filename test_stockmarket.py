# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:58:13 2017

@author: karin
"""

import unittest

from stockmarket import StockMarket
import datetime 

class TestStockMarketFunctions(unittest.TestCase):
    stockmarket=None
    def setUp(self):
        """for all types of stock, create stock object:"""
        self.stockmarket=StockMarket()
        pass
    
    def tearDown(self):
        pass
    
    def test_all_share_index(self):
        """ Calculate the GBCE All Share Index using the geometric mean of prices for all stocks"""
        self.stockmarket.record_trade('TEA',datetime.datetime.now(),2,0,2.0)
        self.assertEquals( self.stockmarket.calculate_all_share_index(),0 )
    
if __name__=='__main__':
    unittest.main()
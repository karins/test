# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:55:11 2017

@author: karin
"""
import unittest

from stock import Stock

class TestStock(unittest.TestCase):
    stocklist=None
    def setUp(self):
        """for all types of stock, create stock object:"""
        self.stocklist={'TEA':Stock('TEA','Common', 0,None,100), 'POP':Stock('POP','Common', 8,None,100) ,
        'ALE':Stock('ALE','Common', 23,None,60),'GIN':Stock('GIN','Preferred', 8,2,100) ,
        'JOE':Stock('JOE','Common', 13,None,250)} 
        
        pass
    
    def tearDown(self):
        pass
    
    
    
    def test_calculate_dividend_yield(self):
        #test prices, test (correct) answers
        prices = [5.0,10.0,20.0]
        stockyields={'TEA':{5.0:0.0,10.0:0.0,20.0:0.0},'POP':{5.0:8.0/5.0, 10.0:8.0/10.0, 20.0:8.0/20.0},
        'ALE':{5.0:23.0/5.0,10.0:23.0/10.0, 20.0:23.0/20.0},'GIN':{5.0:0.02/5.0, 10.0:0.02/10.0, 20.0:0.02/20.0},'JOE':{5.0:13.0/5.0, 10.0:13.0/10.0, 20.0:13.0/20.0}}
        for stock in self.stocklist.values():
            for price in prices:
                if stock.stocktype==stock.stocktypes['Common']:
                    self.assertEqual(stock.get_last_dividend/price, stockyields[stock.stocksymbol][price])
                elif stock.stocktype==stock.stocktypes['Preferred']:
                    self.assertEqual(stock.fixed_dividend_par_value/price,stockyields[stock.stocksymbol][price])
    
    def test_calculate_PE_Ratio(self):
        prices = [5.0,10.0,20.0]
        stockratios={'TEA':{5.0:0.0, 10.0:0.0, 20.0:0.0},'POP':{5.0:5.0/8.0,10.0:10.0/8.0, 20.0:20.0/8.0},
        'ALE':{5.0:5.0/23.0,10.0:10.0/23.0, 20.0:20.0/23.0},'GIN':{5.0:5.0/8.0, 10.0:10.0/8.0, 20.0:20.0/8.0},'JOE':{5.0:5.0/13.0, 10.0:10.0/13.0, 20.0:20.0/13.0}}
    
        for stock in self.stocklist.values():
            for price in prices:
                if stock.get_last_dividend()!=0.0:
                    self.assertEqual(price/stock.get_last_dividend(),stockratios[stock.stocksymbol][price])
    
    """Record a trade, with timestamp, quantity of shares, buy or sell indicator and traded price """
    def test_recording(self):
        """TODO: COMPLETE"""
        pass 
    
    """iv. Calculate Volume Weighted Stock Price based on trades in past 15 minutes """
    def test_calculate_volume_weighted_stock_price(self):
        
        #datetime.datetime.now() - datetime.timedelta(minutes = 15)
        """TODO: COMPLETE"""
        pass
    
if __name__=='__main__':
    unittest.main()
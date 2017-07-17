# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 11:06:44 2017

@author: karin

Stored information on individual trade
"""

class Trade:
    timestamp =0.0
    quantity=0
    """Common=0,Preferred=1"""
    tradetype=1
    price=0.0
    def __init__(self,timestamp, quantity,tradetype,price):
        self.timestamp
        self.quantity
        self.tradetype
        self.price
    def get_timestamp(self):
        return self.timestamp
    def get_quantity(self):
        return self.quantity
    def get_tradetype(self):
        return self.tradetype
    def get_price(self):
        return self.price
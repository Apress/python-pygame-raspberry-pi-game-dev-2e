#!/usr/bin/python

class Item:
    vat_rate = .2
    
    def __init__(self, price):
        self.price = price

    def calcVAT(self):
        return self.price * self.vat_rate

item = Item(2.99)
print (item.calcVAT())

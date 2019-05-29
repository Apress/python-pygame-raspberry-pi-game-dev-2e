#!/usr/bin/python

class UkVat:
    vat_rate = .2

    def calcVAT(self, item):
        return item.price * self.vat_rate

class OntarioVat:
    vat_rate = .13

    def calcVAT(self, item):
        return item.price * self.vat_rate

class Item:
    vat_rate = .2
    
    def __init__(self, price):
        self.price = price

    def calcVAT(self, rate):
        return rate.calcVAT(self)

item = Item(2.99)

uk = UkVat()
ontario = OntarioVat()

print (item.calcVAT(uk))
print (item.calcVAT(ontario))

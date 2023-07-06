#!/usr/bin/env python3
import ipdb
class CashRegister:
    def __init__(self, discount = 0, items = []):
        self.items = []
        self.discount = discount
        self.total = 0
        self.last_item_price = 0
        self.last_item_quantity = 0

    def add_item(self, item, price, quantity = 1):
        self.last_item_quantity = quantity
        self.last_item_price = price
        self.total += (price * quantity)
        if quantity == 1:
            self.items.append(item)
        else:
            self.items+=[item for i in range(quantity)]
            # for i in range(quantity):
            #     self.items.append(item)

    def apply_discount(self):
        if self.discount > 0 and type(self.discount) == type(1):
            self.total = self.total * (1 - (self.discount/100))
            print(f'After the discount, the total comes to ${int(self.total)}.')
        else:
            print('There is no discount to apply.')

    def void_last_transaction(self):
            self.total = self.total - (self.last_item_quantity * self.last_item_price)




# register = CashRegister(20)
# register.add_item("eggs", 2.50)
# register.add_item("milk", 2.50)
# register.apply_discount()
# register.void_last_transaction()
# print(register.total)
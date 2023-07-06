#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0, total = 0, items=[]):
        self.items = items
        self.discount = discount
        self.total = total
    #TODO Need to added items to cart
    def add_item(self, item, price, quantity = 1):
        self.total += (price * quantity)
        if quantity == 1:
            self.items += [item]
        else:
            print("yep")

    def apply_discount(self):
        if self.discount > 0 and type(self.discount) == type(1):
            self.total = self.total * (1 - float(f'.{self.discount}'))
            print(f'After the discount, the total comes to ${int(self.total)}.')
        else:
            print('There is no discount to apply.')

# register = CashRegister()
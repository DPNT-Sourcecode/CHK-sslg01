import string


class CheckoutSolution:

    PRICE = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 80,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 30,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 90,
        "Y": 10,
        "Z": 50,
    }

    DISCOUNTED_PRICE = {
        "A": {
            5: 200,
            3: 130,
        },
        "B": {
            2: 45,
        },
        "H": {
            5: 45,
            10: 80,
        },
        "K": {
            2: 150,
        },
        "P": {
            5: 200,
        },
        "Q": {
            3: 80,
        },
        "V": {
            2: 90,
            3: 130,
        },
    }

    FREE_DISCOUNT = {
        "B": {
            "E": 2,
        },
        "F": {
            "F": 3,
        },
        "M": {
            "N": 3,
        },
        "Q": {
            "R": 3,
        },
        "U": {
            "U": 4,
        },
    }

    def __init__(self):
        self.counter = {}

    def freeItemCount(self, sku):
        if not sku in self.FREE_DISCOUNT: 
            return 0
        itemToMatch = list(self.FREE_DISCOUNT[sku].keys())[0]
        return self.counter[itemToMatch] // self.FREE_DISCOUNT[sku][itemToMatch]

    def freeSkusCounter(self):
        return {
            sku: count - self.freeItemCount(sku)
            for sku, count in self.counter.items()
        }

    def totalSkuPrice(self, sku):
        freeItemsCounter = self.freeSkusCounter()
        price = 0
        remaining = freeItemsCounter[sku]

        if sku in self.DISCOUNTED_PRICE:
            for count in sorted(self.DISCOUNTED_PRICE[sku].keys(), reverse=True):
                price += remaining // count * self.DISCOUNTED_PRICE[sku][count]
                remaining %= count
        
        return price + remaining * self.PRICE[sku]

    # skus = unicode string
    def checkout(self, skus):
        if skus == "": return 0

        self.counter = {
            item: skus.count(item) if skus.find(item) != -1 else 0
            for item in string.ascii_uppercase
        }

        if len(skus) != sum(self.counter.values()): return -1

        return sum(self.totalSkuPrice(sku) for sku in self.counter.keys() if self.counter[sku] > 0)

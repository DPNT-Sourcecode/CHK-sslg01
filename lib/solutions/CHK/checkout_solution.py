from itertools import count
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
            "F": 2,
        },
        "M": {
            "N": 3,
        },
        "Q": {
            "R": 3,
        },
        "U": {
            "U": 3,
        },
    }

    def __init__(self):
        self.counter = {}

    def freeItemCount(self, sku):
        if not sku in self.FREE_DISCOUNT: return 0
        itemToMatch = list(self.FREE_DISCOUNT[sku].keys())[0]
        return self.counter[itemToMatch] // self.FREE_DISCOUNT[sku][itemToMatch]

    def freeItemsCounter(self):
        return {
            sku: count - self.freeItemCount(sku)
            for sku, count in self.counter.items()
        }

    def discountedPrice(self, item):
        if not item in self.DISCOUNTED_PRICE: return 0
        freeItemsCounter = self.freeItemsCounter()
        price = 0
        remaining = freeItemsCounter[item]

        if item in self.DISCOUNTED_PRICE:
            for count in sorted(self.DISCOUNTED_PRICE[item].keys(), reverse=True):
                price += freeItemsCounter[item] // count * self.DISCOUNTED_PRICE[item][count]
                remaining %= count
        
        return price + remaining * self.PRICE[item]

    # def priceA(self, counter):
    #     num5A = counter["A"] // 5
    #     num3A = (counter["A"] % 5) // 3
    #     num1A = (counter["A"] % 5) % 3
    #     return num5A * 200 + num3A * 130 + num1A * 50

    # def priceB(self, counter):
    #     num2E = counter["E"] // 2
    #     num1B = max(counter["B"] - num2E, 0)
    #     return (num1B // 2) * 45 + (num1B % 2) * 30

    # def priceF(self, counter):
    #     num3F = counter["F"] // 3
    #     return (counter["F"] - num3F) * 10

    # skus = unicode string
    def checkout(self, skus):
        if skus == "": return 0

        self.counter = {
            item: skus.count(item) if skus.find(item) != -1 else 0
            for item in string.ascii_uppercase
        }

        if len(skus) != sum(self.counter.values()): return -1

        return sum(self.discountedPrice(item) for item in self.counter.keys())
        # price = self.priceA(counter)
        # price += self.priceB(counter)
        # price += counter["C"] * 20
        # price += counter["D"] * 15
        # price += counter["E"] * 40
        # price += self.priceF(counter)

        # return price

if __name__ == "__main__":
    checkout = CheckoutSolution()
    print(checkout.checkout("AABABABABAA"))
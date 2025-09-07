import string


class CheckoutSolution:

    def priceA(self, counter):
        num5A = counter["A"] // 5
        num3A = (counter["A"] % 5) // 3
        num1A = (counter["A"] % 5) % 3
        return num5A * 200 + num3A * 130 + num1A * 50

    def priceB(self, counter):
        num2E = counter["E"] // 2
        num1B = max(counter["B"] - num2E, 0)
        return (num1B // 2) * 45 + (num1B % 2) * 30

    def priceF(self, counter):
        num3F = counter["F"] // 3
        return (counter["F"] - num3F) * 10

    # skus = unicode string
    def checkout(self, skus):
        if skus == "": return 0

        counter = {
            item: skus.count(item) if skus.find(item) != -1 else 0
            for item in string.ascii_uppercase
        }

        if len(skus) != sum(counter.values()): return -1

        price = self.priceA(counter)
        price += self.priceB(counter)
        price += counter["C"] * 20
        price += counter["D"] * 15
        price += counter["E"] * 40
        price += self.priceF(counter)

        return price
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if skus == "": return 0

        counter = {
            item: skus.count(item) if skus.find(item) != -1 else 0
            for item in "ABCDEF"
        }

        if len(skus) != sum(counter.values()): return -1

        num5A = counter["A"] // 5
        num3A = (counter["A"] % 5) // 3
        num1A = (counter["A"] % 5) % 3

        num2E = counter["E"] // 2
        num1B = max(counter["B"] - num2E, 0)

        price = num5A * 200 + num3A * 130 + num1A * 50
        price += (num1B // 2) * 45 + (num1B % 2) * 30
        price += counter["C"] * 20
        price += counter["D"] * 15
        price += counter["E"] * 40

        return price
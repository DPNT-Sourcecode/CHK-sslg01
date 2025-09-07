class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if skus == "": return 0

        counter = {
            "A": skus.count("A") if skus.find("A") != -1 else 0,
            "B": skus.count("B") if skus.find("B") != -1 else 0,
            "C": skus.count("C") if skus.find("C") != -1 else 0,
            "D": skus.count("D") if skus.find("D") != -1 else 0,
            "E": skus.count("E") if skus.find("E") != -1 else 0
        }

        if len(skus) != sum(counter.values()): return -1

        num5A = counter["A"] // 5
        num3A = (counter["A"] % 5) // 3
        num1A = (counter["A"] % 5) % 3

        num2E = counter["E"] // 2
        num1B = counter["B"] - num2E

        price = num5A * 200 + num3A * 130 + num1A * 50
        price += (num1B // 2) * 45 + (num1B % 2) * 30
        price += counter["C"] * 20
        price += counter["D"] * 15

        return price


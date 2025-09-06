
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if skus == "": return 0

        if skus.find("^[^A-D]$") != -1: return -1

        counter = {
            "A": skus.count("A"),
            "B": skus.count("B"),
            "C": skus.count("C"),
            "D": skus.count("D")
        }

        price = counter["A"] // 3 * 130 + counter["A"] % 3 * 50
        price += counter["B"] // 2 * 45 + counter["B"] % 2 * 30
        price += counter["C"] * 20
        price += counter["D"] * 15

        return price

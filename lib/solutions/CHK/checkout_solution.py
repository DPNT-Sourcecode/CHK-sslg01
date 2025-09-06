
import re


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if skus == "": return 0

        print(skus)
        if skus.find("^[^A-D]+$") != -1: return -1

        counter = {
            "A": skus.count("A") if skus.find("A") != -1 else 0,
            "B": skus.count("B") if skus.find("B") != -1 else 0,
            "C": skus.count("C") if skus.find("C") != -1 else 0,
            "D": skus.count("D") if skus.find("D") != -1 else 0
        }

        price = counter["A"] // 3 * 130 + counter["A"] % 3 * 50
        price += counter["B"] // 2 * 45 + counter["B"] % 2 * 30
        price += counter["C"] * 20
        price += counter["D"] * 15

        return price

if __name__ == "__main__":
    checkout_solution = CheckoutSolution()
    print(checkout_solution.checkout("i"))
    # print(checkout_solution.checkout("ABCD"))
    # print(checkout_solution.checkout("AABCD"))
    # print(checkout_solution.checkout("AABCDD"))
    # print(checkout_solution.checkout("AABCDDD"))
    # print(checkout_solution.checkout("AABCDDDD"))
    # print(checkout_solution.checkout("AABCDDDDD"))



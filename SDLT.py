class Solution:
    def calculatelbtt(price: float| int ) -> int | float:
        print(type(price))
        if price < 0:
            raise Exception("Sorry, no numbers below zero")
        if price <= 125000:
            return 0
        elif price <= 250000:
            return (price - 125000) * 0.02
        elif price <= 925000:
            return (price - 250000) * 0.05 + 2500
        elif price <= 1500000:
            return (price - 925000) * 0.10 + 36250
        else:
            return (price - 1500000) * 0.12 + 93750

if __name__ == "__main__":
    print('\n*** Get the stamp duty land tax ***\n')

    price = input("\nPlease enter price: ")

    tax = Solution.calculatelbtt(int(price))
    print("\n")
    print(tax)










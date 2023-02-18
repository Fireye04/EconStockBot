import random

# List of stock name strings.
# Looks like this: ["YOUR", "MOM", "IS", "GAY"]
stocks = []

# Decimal list of % makeup of stocks within the list
# only really useful when weighting certain stocks over others
# Looks like this: [6.9, 4.20, 3.14, 0.1]
# Note: must have identical length to stock list
weights = []

# a number to multiply the weights by to attain a minimum of one in the smallest weight value. (no decmials)
# usually a factor of 10
multiplier = 10

# a list of integers (no decmials) attained by multiplying each weight by the multiplier and rounding
# to the nearest whole number
# Looks like this: [69, 42, 31, 1]
multipliers = []

# deprecated
pairsW = []

# paired list of stocks and weights
# looks like this: [["YOUR", 69], ["MOM", 42], ["IS", 31], ["GAY", 1]]
pairs = []

# final list of weighted choices to randomly select from.
# if you don't have weights, just put your stock list here
final = []

# how many stocks you want chosen from the list
numStocks = 10


def main():
    # To get a set of lists, just run the following command:
    listCalc(stocks, weights, multiplier)
    # then paste the printed lists into each corresponding variable within the code

    # From there, run this
    print(random.sample(final, numStocks))
    # and boom, you have a buncha random stocks


# ----- Everything below this point is just calculations ----- #

def listCalc(stonks, weightss, multiplierr):
    multiplierss = multiplierCalc(weightss, multiplierr)
    print(f"multipliers- {multiplierss}")

    pairssW = pairCalc(stonks, weightss)
    print(f"pairsW- {pairssW}")

    pairss = pairCalc(stonks, multiplierss)
    print(f"pairs- {pairss}")

    finall = finalCalc(pairss)
    print(f"final- {finall}")


def finalCalc(pairs):
    Final = []
    for i in range(len(pairs)):
        for j in range(pairs[i][1]):
            Final.append(pairs[i][0])
    return Final


def multiplierCalc(weights, multiplier):
    Multiplier = []

    for i in range(len(weights)):
        Multiplier.append(round(weights[i] * multiplier))

    return Multiplier


def pairCalc(stocks, weights):
    pairs = []
    for i in range(len(stocks)):
        pairs.append([stocks[i], weights[i]])
    return pairs


if __name__ == '__main__':
    main()

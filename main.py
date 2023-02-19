import random

# List of stock name strings. These are all the stocks the program can buy from
# Looks like this: ["YOUR", "MOM", "IS", "GAY"]
stocks = []

# Decimal list of % makeup of stocks within the list
# only really useful when weighting certain stocks over others
# Looks like this: [6.9, 4.20, 3.14, 0.1]
# Note: must have identical length to stock list
weights = []

# a number to multiply the weights by to attain a minimum of one in the smallest weight value. (no decmials)
# usually a factor of 10
weightMultiplier = 10

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

# ----- INFO -----

# Spendable money
funds = 0

# money inside stock
fundsInStock = 0

# The stocks that you have money in right now and none.
# none represents unspent funds and must always be at the end
# looks like this ["YOUR", "MOM", "GAY", "none"]
myStocks = ["none"]

# how much money you have in each stock (thousands) and funds
# funds represents unspent money, and must always be at the end
# looks like this [4200, 12539, 6900, funds]
myWeights = [funds]

# converts thousands to ones. Increase this number to kill your pc and get more granular/ detailed outputs
multiplier = 0.001

# distribution of your stock. similar to final, however, this is yours and final is the pool of available
# purchasable stock
myFinal = []

# ----- INFO -----

# default percent of available funds/stock to sell/buy
defaultPercent = 10


def main():
    # To get a set of lists, just run the following command:

    print("\n----- Available Stocks -----")
    listCalc(stocks, weights, weightMultiplier)
    print("----- Available Stocks -----\n")

    print("----- Your Stocks -----")
    listCalc(myStocks, myWeights, weightMultiplier)
    print("----- Your Stocks -----")

    # then paste the printed lists into each corresponding variable within the code

    # determines amount to buy and/or sell based on given variables
    print("\n----- Buy -or- Sell -----")
    print(f"sell {sellStock()} at ${int(1 / multiplier)} per listed option")
    print(f"buy {buyStock()} at ${int(1 / multiplier)} per listed option")
    print("----- Buy -or- Sell -----")


# ----- Everything below this point is just calculations ----- #

def buyStock(percent=defaultPercent):
    # get percentage of available funds to invest
    buy = funds * (percent / 100)

    # turn said percentage into a usable int
    buy = round(buy * multiplier)

    return random.sample(final, buy)


def sellStock(percent=defaultPercent):
    # get percentage of available funds to invest
    sell = fundsInStock * (percent / 100)

    # turn said percentage into a usable int
    sell = round(sell * multiplier)

    return random.sample(myFinal, sell)


def listCalc(stonks, weightss, multiplierr):
    multiplierss = multiplierCalc(weightss, multiplierr)
    print(f"multipliers = {multiplierss}\n")

    print(f"multiplier = {multiplierr}\n")

    pairssW = pairCalc(stonks, weightss)
    print(f"pairsW = {pairssW}\n")

    pairss = pairCalc(stonks, multiplierss)
    print(f"pairs = {pairss}\n")

    finall = finalCalc(pairss)
    print(f"final = {finall}")


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

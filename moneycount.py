#Somebody challenged me to come up with how many collections of coins can make a dollar
#Coins of the same type are indistinguishable, order does not matter
#We're only using your standard penny, nickel, dime, quarter, though the configuration array could easily be altered to include nonstandard (such as half dollars) or nonexistent coins (such as 30 cent pieces)

coins = [1,5,10,25]

def coinCount (coinTypes, target):
    sum = 0
    curr = 0
    while (curr < target):
        if(len(coinTypes) > 1):
            sum = sum + coinCount(coinTypes[1:], target - curr)
        curr = curr + coinTypes[0]
        if(curr == target):
            sum = sum + 1
    return sum

print(coinCount(coins,100))

# coin problem 

def coin_change(coins, amount):
  #sort the coins
  coins.sort(reverse=True)
  #create a list to store the coins used
  coins_used = []

  while amount > 0:
    coin = 0
    for coin in coins:
      if coin <= amount:
        coins_used.append(coin)
        amount -= coin
        break 

  print(f"Coins used: {coins_used}")


coins = [1,5,10,15]
amount = 14

coin_change(coins, amount)

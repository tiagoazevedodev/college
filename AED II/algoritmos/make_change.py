def make_change(value):
    coins = [100, 50, 25, 10, 5, 1]
    used_coins = []
    total = 0
    while(value != total):
        for coin in coins:
            if total + coin <= value:
                total += coin
                used_coins.append(coin)
                break
    return used_coins

print(make_change(67))
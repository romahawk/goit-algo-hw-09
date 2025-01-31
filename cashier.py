# function 1
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

# Приклад використання:
amount = 113
greedy_result = find_coins_greedy(amount)
print(f"Жадібний алгоритм для суми {amount}: {greedy_result}")

# function 2
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [0] + [float('inf')] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
    # Відновлення результату
    result = {}
    i = amount
    while i > 0:
        for coin in coins:
            if dp[i] == dp[i - coin] + 1:
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                i -= coin
                break
    return result

# Приклад використання:
dp_result = find_min_coins(amount)
print(f"Динамічне програмування для суми {amount}: {dp_result}")

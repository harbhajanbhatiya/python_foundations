def process_prices(prices):
    discounted_prices = list(map(lambda x: x * 0.9, prices))
    return discounted_prices
    filtered_prices = list(filter(lambda x: x > 300, discounted_prices))
    return filtered_prices

prices=[100,500,900,50,750]
result= process_prices(prices)
print("Final Prices after discount and filtering:", result)
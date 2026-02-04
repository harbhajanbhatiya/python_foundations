def apply_discount(price,discount_percent=5):
    discount_amount = price * (discount_percent / 100)
    discounted_price = price - discount_amount
    return discounted_price

print(apply_discount(1000))          # Using default discount of 5%
print(apply_discount(1000, 10))      # Using custom discount of 10)
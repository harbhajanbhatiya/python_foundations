orders=[1200,2500,800,1750,3000]
total_revenue=0
for order in orders:
    if order<1000:
        final_amount=order
    elif 1000<=order<2000:
        discount=0.05*order
        final_amount=order-discount
    elif 2000<=order<3000:
        discount=0.10*order
        final_amount=order-discount
    else:
        discount=0.15*order
        final_amount=order-discount
    total_revenue+=final_amount
print(f"Total revenue after discounts: {total_revenue}")
discounted_orders=sum(1 for order in orders if order>=1000)
print(f"Number of orders that received a discount: {discounted_orders}")
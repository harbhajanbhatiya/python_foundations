order_amount=int(input("Enter the order amount: "))
if order_amount>=2000:
    discount=0.15
elif order_amount>=1500 and order_amount<2000:
    discount=0.10
elif order_amount>=1000 and order_amount<1500:
    discount=0.05
else:
    discount=0.0
discount_amount=order_amount*discount
final_amount=order_amount-discount_amount
print("The final amount after discount is:",final_amount)
# Add 5% tax on the final amount
tax=0.05
tax_amount=final_amount*tax
final_amount_with_tax=final_amount+tax_amount
print("The final amount after adding tax is:",final_amount_with_tax)
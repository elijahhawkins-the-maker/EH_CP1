price_apple = 0.99
price_bread = 2.50
price_milk = 3.25

qty_apple = 4
qty_bread = 2
qty_milk = 1

subtotal = (price_apple * qty_apple) + (price_bread * qty_bread) + (price_milk * qty_milk)

tax_rate = 0.08
tax = subtotal * tax_rate

total = subtotal * tax_rate

discount = 0
if total > 10:
    discount = 1.50
    total -= discount

print("subtotal: $", round(subtotal, 2))

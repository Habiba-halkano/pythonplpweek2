def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_price = price * discount_percent / 100
        final_price = price - discount_price
        return f"discount has been applied and final price is {final_price}"
    else:
        return f"no discount applied, original price is {price}"

# print(calculate_discount(1000, 50))
price = float(input("Enter the price:"))
discount_percent = float(input("Enter the discount percent:"))
print(calculate_discount(price, discount_percent))
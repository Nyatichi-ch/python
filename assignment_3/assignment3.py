def calculate_discount(price, discount_percent):
    """
    Calculate the discounted price based on the original price and discount percentages.
    """

    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount

    # If intended: enforce minimum 20% discount
    if discount_percent >= 20:
        return final_price
    else:
        return price
    
discount_percent = float(input("Enter the discount percentage: "))
price = float(input("Enter the original price: "))

final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:              
    print(f"Final price after discount: {final_price:.2f}")

else:
    print(f"No discount applied. Original price: {price:.2f}")    

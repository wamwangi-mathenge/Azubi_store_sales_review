products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Calculate the total price average for all products

average_price = sum(prices) / len(prices)
print(average_price)

print()

new_price_list = []
for price in prices:
    new_price = int(price) - 5
    new_price_list.append(new_price)
    
print(new_price_list)

print()
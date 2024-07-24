#Apply for loops to calculate the total cost of items in a shopping cart.
cart = [9, 3, 19.01, 3.99, 5.46, 15]

calc_result = 0

for price in range(len(cart)):
    calc_result += cart[price]

print(f"The total cost of your shopping cart is ${calc_result}")
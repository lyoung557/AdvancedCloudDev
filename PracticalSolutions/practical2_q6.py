# Practical 2, Question 6
#
# Caclulate the final price of a product after tax and shipping

# Ask the user to input the net price (before tax), sales tax rate and shipping cost

# The price of the product must be greater than zero
product_price_is_valid = False
while product_price_is_valid is False:
	try:
		product_price = float(input('Enter the price of the product before tax: '))
		if product_price > 0.0:
			product_price_is_valid = True
	except ValueError:
		print('Please enter a number greater than zero.')

# The sales tax must be a decimal value between 0 and 1
sales_tax_is_valid = False
while sales_tax_is_valid is False:
	try:
		sales_tax = float(input('Enter the sales tax rate (as a decimal value between 0 and 1): '))
		if sales_tax >= 0.0 and sales_tax <= 1.0:
			sales_tax_is_valid = True
	except ValueError:
		pass

# The shipping cost must be greater than or equal to zero (it is possible that a seller offers free shipping)
shipping_cost_is_valid = False
while shipping_cost_is_valid is False:
	try:
		shipping_cost = float(input('Enter the shipping cost: '))
		if shipping_cost >= 0.0:
			shipping_cost_is_valid = True
	except ValueError:
		print('Please enter a number equal to or greater than zero.')

# If the price of the product is greater than £100, then apply a discount
if product_price > 100:
	discount = 0.1
	print('A discount of 10% will be applied to the price of the product before sales tax and shipping costs.')
else:
	discount = 0

# Calculate and display the total price
total_price = ((product_price * (1 - discount)) * (sales_tax + 1)) + shipping_cost
print(f'The total price is £{total_price:.2f}.')

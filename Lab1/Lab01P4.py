#
# Catarina Pottle
# 1-14-22
# This program calculates the cost
# for the total purchase of books including
# 7% sales tax on the total
#

# Named constants because values don't change
COST_PER_PAPERBACK = 2.50
COST_PER_HARDBACK = 7.00
COST_PER_MAGAZINE = 3.95
SALES_TAX = 0.07

# Get number of books selected for.
paperback = float(input('Enter the number of paperback books: '))
hardback = float(input('Enter the number of hardback books: '))
magazine = float(input('Enter the number of magazines: '))

# Cost of books without sales tax.
book_cost = ((COST_PER_PAPERBACK*paperback) +
             (COST_PER_HARDBACK*hardback) +
             (COST_PER_MAGAZINE*magazine))

# Calculated sales tax based on the total number of books purchased.
calculated_sales_tax = (book_cost * SALES_TAX)

# Cost of books with 7% sales tax.
total_cost = book_cost + calculated_sales_tax

# Display cost at each stage before sales tax, the sales tax, and after sales tax.
print(f' Cost before tax: ${book_cost:.2f}')
print(f' Sales tax: ${calculated_sales_tax:.2f}')
print(f' Cost after tax: ${total_cost:.2f}')

#
# Catarina Pottle
# 1-14-22
# This program converts a user-entered Fahrenheit temperature and
# converts it to Celsius
#

# Get the Fahrenheit temperature.
fahrenheit = float(input("Enter a Fahrenheit temperature: "))

# Calculate the Celsius equivalent.
celsius = (fahrenheit - 32) * (5.0 / 9.0)

# Display the Celsius temperature.
print(f'That is equal to {celsius:.2f}', 'degrees Celsius.')

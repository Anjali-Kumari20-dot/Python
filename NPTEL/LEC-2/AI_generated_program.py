# Write a program to convert a given 
# temperature in Celsius to Fahrenheit.

# step 1 : Get the temperature in Celsius from user
celsius = float(input('Enter temperature in Celsius: '))

# step 2 : Convert the temperature to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# step 3 : Print the temperature in Fahrenheit
print(f'{celsius} degrees celsius is equal to: {fahrenheit} degrees Fahrenheit')
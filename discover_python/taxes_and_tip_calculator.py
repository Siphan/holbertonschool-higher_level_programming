""" Creator: Siphan Bou. 
    Name program: Taxes and tip calculator
    Function: Calculates the total amount you have to pay in a restaurant that includes tax and tip
"""

print "Welcome to the taxes and tip calculator!" # Prints a welcome message to user
meal = float(raw_input("What is the price before tax? ")) # Prompts user to enter price before tax. Accepts decimal numbers.
tax = float(raw_input("What are the taxes? (in %) ")) # Prompts user to enter tax rate. Accepts decimal numbers.
meal = meal + meal * tax / 100 # Calculates price of meal after tax 
tip = float(raw_input("What do you want to tip? (in %) ")) # Prompts user to enter tip percentage. Accepts decimal numbers.
total = meal + meal * tip / 100 # Calculates price of meal after tax and tip
print "The price you need to pay is: $%.6f." % total # Outputs calculated total amount in USD.

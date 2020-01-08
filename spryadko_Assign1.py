# My name is Sofya. This program computes cost of a beverage.
# The program asks for the customer's name.
name = input("Hello, what is your name?")
if name.isalpha():
    print("Welcome,"+name+"!")
else:
    print("Sorry, the name should contain only letters.")
    exit()

# The program asks for the type of a beverage a customer wants.
beverage = input("What would you like to drink? Tea or Coffee?").lower()
if beverage == "coffee" or beverage == "c":
    beverage = "coffee"
elif beverage == "tea" or beverage == "t":
    beverage = "tea"
else:
    print("We do not know about this drink. We only have tea or coffee.")
    exit()

# The program asks for the size of the preferred beverage.
size = input("What size of "+beverage+" would you like?").lower()
if size == "small" or size == "s":
    size = "small"
    sizePrice = 1.5
elif size == "medium" or size == "m":
    size = "medium"
    sizePrice = 2.5
elif size == "large" or size == "l":
    size = "large"
    sizePrice = 3.25
else:
    print("This size is not available, size can be only small, medium or large.")
    exit()

# The programs asks to choose a flavor for the customer's beverage.
flavor = input("What flavour would you like? You can choose only one. We have vanilla, chocolate, maple or none for coffee, and lemon, mint or none for tea.").lower()
if (flavor == "vanilla" or flavor == "v") and beverage == "coffee":
    flavor = "vanilla flavor"
    flavorPrice = 0.25
elif (flavor == "chocolate"or flavor == "c") and beverage == "coffee":
    flavor = "chocolate flavor"
    flavorPrice = 0.75
elif (flavor == "maple" or flavor == "m") and beverage == "coffee":
    flavor = "maple flavor"
    flavorPrice = 0.50
elif (flavor == "mint" or flavor == "m") and beverage == "tea":
    flavor = "mint falvor"
    flavorPrice = 0.5
elif (flavor == "lemon"or flavor == "l") and beverage == "tea":
    flavor = "lemon flavor"
    flavorPrice = 0.25
elif flavor == " " or flavor == "none" or flavor == "":
    flavor = "no flavoring"
    flavorPrice = 0.0
else:
    print("Sorry, this flavor is not available.")
    exit()

# The program computes final price of the beverage with tax included and displays the specifications of the beverage as well as the price.
cost = sizePrice + flavorPrice
taxRate = 0.11
finalCost = round(cost + taxRate * cost, 2)
print("For "+name+", a "+size+" "+beverage+", "+flavor+", cost:$"+str(finalCost)+".")




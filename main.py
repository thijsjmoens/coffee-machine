MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# --- The functions ---
    
# Function to process the money
def process_money(coffee):
    
    # Variable for checking enough coins
    not_enough_coins = True
    
    # Check the price for the coffee
    cost_price_coffee = MENU[coffee]['cost']
    
    # Print the price of the coffee
    print(f"This {coffee} costs ${cost_price_coffee}.")
    print('Please insert coins')
    
    # Check if there is enough money added
    while not_enough_coins:
        
        # Ask the user for input
        quarters = round(float(input("How many quarters?: ")), 3) # Must be float, quarters = $0.25
        dimes =  round(float(input("How many dimes?: ")), 3) # Must be float, dimes = $0.10
        nickles =  round(float(input("How many nickles?: ")), 3) # Must be float, nickles = $0.05
        pennies =  round(float(input("How many pennies?: ")), 3) # Must be float, pennies = $0.01
            
        # Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
        total_inserted_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    
        if cost_price_coffee > total_inserted_money:
            
            print("Sorry that's not enough money. Money refunded. Try again")
            not_enough_coins = True
            
        else:
            not_enough_coins = False
            
        
    # Subtract cost price of the inserted money
    change = total_inserted_money - cost_price_coffee
    change_in_dollars = round(change, 3)
    
    # Give back the change
    print(f"Here is ${change_in_dollars} in change.")
    
    # Add cost price to the resources
    if 'money' in resources:
        resources['money'] = resources['money'] + cost_price_coffee    
    else: 
        resources['money'] = cost_price_coffee 


# This function makes the coffee
def make_coffee(coffee):
    
    # Step 1: Check the ingredients of the coffee    
    water = MENU[coffee]['ingredients']['water']
    milk = MENU[coffee]['ingredients']['milk']
    coffee_beans = MENU[coffee]['ingredients']['coffee'] 
    
    # Step 2: Check resources sufficient?
    if resources['water'] < water:
        print("Sorry there is not enough water.")
        
    elif resources['milk'] < milk: 
        print("Sorry there is not enough milk.")
        
    elif resources['coffee'] < coffee_beans: 
        print("Sorry there are not enough coffee beans.")
        
    # Step 3: process the money for the coffee
    process_money(coffee)

    # Step 4: Make Coffee and deducte ingredients from resources
    resources['water'] = resources['water'] - water
    resources['milk'] = resources['milk'] - milk    
    resources['coffee'] = resources['coffee'] - coffee_beans
        
    # Step 5: Print if coffee is ready
    print(f"Here's your {coffee} ☕ Enjoy!")
    

# Function to print the report to the screen
def print_report():
    
    # Assign resources to variables    
    water = resources['water']
    milk = resources['milk']    
    coffee_beans = resources['coffee']
        
    # Check if there is any money yet
    if 'money' in resources:
        money = resources['money']     
    else:
        money = 0.00
    
    # Print the resources
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee_beans}g")    
    print(f"Money: ${money}")    



# ---- ☕ THE COFFEE MACHINE --- 

# Create a check variable for valid input of user
check_valid_inpput = True

# Check if the input of the user is valid
# The input can be coffee (espresso/latte/cappuccino) or report or off
while check_valid_inpput:

    # Ask the user for coffee with the prompt: What would you like? (espresso/latte/cappuccino):'
    ask_user = input('What would you like? ')
        
    # If the user want coffee
    if ask_user == 'espresso' or ask_user == 'latte' or ask_user == 'cappuccino':
        
        # Make the coffee
        make_coffee(ask_user)
        
    # If the user wants a report
    elif ask_user == 'report':
        
        # Print the report
        print_report()
        
    # If the user want to shut off this machine
    elif ask_user == 'off':
        
        # Shut down the machine
        exit()
        
    # If user gives a wrong input
    else:
        
        # Set the check to false
        check_valid_inpput = False
        
    
    
    # The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
    
# 2. Turn off the Coffee Machine by entering “ off ” to the prompt.


# 3. Print report.

    # When the user enters “report” to the prompt, a report should be generated that shows
    # the current resource values. e.g.
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5
    
    
# 4. Check resources sufficient?

    # When the user chooses a drink, the program should check if there are enough resources to make that drink.

    # if not enough resource, print: “ Sorry there is not enough water. ” and don't make the coffee
    # The same should happen if another resource is depleted, e.g. milk or coffee.
    
    
# 5. Process coins
    
    # If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.

    # Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    
    # Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
    
    
# 6. Check transaction successful?

    # Check that the user has inserted enough money to purchase the drink they selected. 
    # E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “ Sorry that's not enough money. Money refunded. ”.

    # But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g.
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5

    # If the user has inserted too much money, the machine should offer change.  “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
    
    
# 7. Make Coffee.

    # If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the
    # coffee machine resources.
    # E.g. report before purchasing latte:
    # Water: 300ml
    # Milk: 200ml
    # Coffee: 100g
    # Money: $0
    # Report after purchasing latte:
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5
        # b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.
    
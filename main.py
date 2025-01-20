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

# Function to check sufficient resources
def check_resources(coffee):
    
    if resources['water'] < MENU[coffee]['ingredients']['water']:
        print("Sorry there is not enough water.")
        return True

    elif resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
        print("Sorry there are not enough coffee beans.")
        return True
            
    else: 
        return False
    
    # Check also for milk
    if 'milk' in resources:   
    
        if resources['milk'] < MENU[coffee]['ingredients']['milk']:
            print("Sorry there is not enough milk.")
            return True

    
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
    coffee_beans = MENU[coffee]['ingredients']['coffee'] 
    
    if 'milk' in coffee:
        milk = MENU[coffee]['ingredients']['milk']

        
    # Step 2: process the money for the coffee
    process_money(coffee)

    # Step 3: Make Coffee and deduct ingredients from resources
    resources['water'] = resources['water'] - water
    resources['coffee'] = resources['coffee'] - coffee_beans
    
    if 'milk' in coffee:
        resources['milk'] = resources['milk'] - milk    

        
    # Step 4: Print if coffee is ready
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
check_valid_input = True

# Check if the input of the user is valid
# The input can be coffee (espresso/latte/cappuccino) or report or off
while check_valid_input:
    
    # Ask the user for coffee with the prompt: What would you like? (espresso/latte/cappuccino):'
    input_user = input('What would you like? ')
        
    # If the user want coffee
    if input_user == 'espresso' or input_user == 'latte' or input_user == 'cappuccino':
        
        # Check resources
        while check_resources(input_user):
            
            # Ask the user for coffee with the prompt: What would you like? (espresso/latte/cappuccino):'
            input_user = input('What would you like? ')
        
        # Make the coffee
        make_coffee(input_user)
        
    # If the user wants a report
    elif input_user == 'report':
        
        # Print the report
        print_report()
        
    # If the user want to shut off this machine
    elif input_user == 'off':
        
        # Shut down the machine
        exit()
        
    # If user gives a wrong input
    else:
        
        # Set the check to false
        check_valid_input = False
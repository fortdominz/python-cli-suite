
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
coins = {
    "pennies": 0.01,
    "nickels": 0.05,
    "dimes": 0.1,
    "quarters": 0.25,
}


profit = 0
order = 0

machine_on = True

while machine_on:
    # TODO: 1. Prompt user by asking “What would you like?
    user_choice = input("What would you like? (espresso/latte/cappuccino): \n").lower()

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == "off":
        machine_on = False

    # TODO: 3. Print report.
    elif user_choice == "report":
        # for keys in resources:
        #     print(f"{keys}: {resources[keys]}")
        # print(f"Money: ${money}")
        print("Resource Report:")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")


    # TODO: 4. Check resources sufficient?
    # elif user_choice == "espresso" or user_choice == "cappuccino" or user_choice == "latte":
    elif user_choice in MENU:
        drink = MENU[user_choice] # This pulls the full data for the chosen drink from the MENU dictionary; this includes its ingredients and cost.
        ingredients = drink["ingredients"] # Now we're digging into just the ingredients part of the drink (like water, milk, and coffee amounts) and storing it in a variable to make it easier to work with.
        # Step 1: Check if all required ingredients are available
        can_make = True # Start with the assumption that we can make the drink. We'll flip this to False if we discover a problem.

        for item in ingredients: # Loop through each required ingredient needed to make the selected drink.
            if ingredients[item] > resources[item]: # Compare required vs. available. If we don’t have enough of an ingredient, let the user know and stop checking further.
                print(f"Sorry, there is not enough {item}.")
                can_make = False
                break

        # TODO: 7.  Make Coffee.
        # Step 2: If we can make it, deduct resources
        if can_make:
            # TODO: 5. Process coins.
            # Prompt for coins
            print("Insert coins to purchase drink...\n")
            n_pennies = int(input("How many pennies? "))
            n_nickels = int(input("How many nickels? "))
            n_dimes = int(input("How many dimes? "))
            n_quarters = int(input("How many quarters? "))

            # calculate total inserted coins
            total_coin_inserted = (
                n_pennies * coins["pennies"] +
                n_nickels * coins["nickels"] +
                n_dimes * coins["dimes"] +
                n_quarters * coins["quarters"]
            )

            # Step 3: Retrieve Drink Cost & Compare Inserted Money to Cost
            drink_cost = drink["cost"]

            # TODO: 6. Check transaction successful?
            if total_coin_inserted >= drink_cost:
                # Calculate and Return Change
                change = round(total_coin_inserted - drink_cost, 2)
                if change >= 0:
                    order += 1

                profit += drink_cost # Adds to machine's earnings

                # Step 4: Deduct Used Ingredients from resources
                for item in ingredients:
                    resources[item] -= ingredients[item]

                print("\n" * 2000)
                print(f"Your Order has been taken. You are Order {order}")
                print(f"You have a change of ${change}")
                print(f"Here is your {user_choice}. Enjoy!")
                print(f"Next customer, please.\n")

            else:
                print(f"Sorry, that's not enough money for {user_choice}. Refunded ${round(total_coin_inserted, 2)}.")

    else:
        print("Invalid input. Please type espresso, latte, cappuccino, report to view available resources or off to power off the machine. ")


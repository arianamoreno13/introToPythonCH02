#program that calculates final price of an order(someone went to a market and bought apples/bananas)
"""Write a python program that has 4 functions
"""


#function that asks user to 'enter the number of fruits in the bag'.
def get_fruits_count():
    try:
        num_fruits = int(input("Please enter the number of fruit in the bag: "))
        #returns whatever number the user entered.
        return num_fruits
        #num_apples = int(input("Please enter the number of apples in the bag: "))
        #num_bananas = int(input("Please enter the number of bananas in the bag: "))
        #return num_apples(), num_bananas()

    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_fruits_count()

#calculates price of bag of apples. receives number of apples in bag, multi by 3 ($3 per apple)
def calculate_apples_price(num_apples):
    #returns price of bag of apples
    return num_apples * 3

#calculates price of bag of bananas. receives number of banana in bag, multi by 2 ($2 per banana)
def calculate_bananas_price(num_bananas):
    """returns price of bag of banana"""
    return num_bananas * 2

#Function print_final_bill
def print_final_bill(apples_price, bananas_price):
    #print bill in a nice manner
    print(f"You bought ${bananas_price} worth of bananas, and ${apples_price} worth of apples.Your total is ${apples_price + bananas_price}.")

# Function calls
num_apples = get_fruits_count()
num_bananas = get_fruits_count()

apples_price = calculate_apples_price(num_apples)
bananas_price = calculate_bananas_price(num_bananas)

print_final_bill(apples_price, bananas_price)

"""Write a python program that has 4 functions
"""
#For this homework, you will write a program that calculates the final price of an order that contains a bag of
#apples and a bag of bananas. (i.e. someone went to a supermarket and bought some apples and bananas)

"""function that asks user to 'enter the number of fruits in the bag'."""
def get_fruits_count():
    try:
        num_fruits = int(input("Please enter the number of fruits in the bag: "))
        """returns whatever number the user entered."""
        return num_fruits
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_fruits_count()

"""function calculates price of bag of apples. receives number of apples in bag, multi by 3 ($3 per apple)""" 
def calculate_apples_price(num_apples):
    """returns price of bag of apples"""
    return num_apples * 3

"""function calculates price of bag of bananas. receives number of banana in bag, multi by 2 ($2 per banana)"""
def calculate_bananas_price(num_bananas):
    """returns price of bag of banana"""
    return num_bananas * 2

"""Function print_final_bill"""
def print_final_bill(apples_price, bananas_price):
    """print bill in a nice manner"""
    print(f"Thank you for shopping with us. You bought ${bananas_price} worth of bananas and ${apples_price} worth of apples.Your total bill is ${apples_price + bananas_price}.")

# Function calls
num_apples = get_fruits_count()
num_bananas = get_fruits_count()

apples_price = calculate_apples_price(num_apples)
bananas_price = calculate_bananas_price(num_bananas)

print_final_bill(apples_price, bananas_price)

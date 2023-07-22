"""Write a python program that has 4 functions
"""
#For this homework, you will write a program that calculates the final price of an order that contains a bag of
#apples and a bag of bananas. (i.e. someone went to a supermarket and bought some apples and bananas)

#function that asks user to 'enter the number of fruits in the bag'. This function returns whatever number the user entered. receives no parameter, but returns the number of fruits
def get_fruits_count():
    try:
        num_fruits = int(input("Please enter the number of fruits in the bag: "))
        return num_fruits
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_fruits_count()

#A function calculates price of bag of apples. receives number of apples in bag, multi by 3 ($3 per apple) and returns price of bag of apples
def calculate_apples_price(num_apples):
    return num_apples * 3

#A function calculates price of bag of bananas. receives number of banana in bag, multi by 2 ($2 per banana) and returns price of bag of banana
def calculate_bananas_price(num_bananas):
    return num_bananas * 2

def print_final_bill(apples_price, bananas_price):
    print(f"Thank you for shopping with us. You bought ${bananas_price} worth of bananas and ${apples_price} worth of apples.
          Your total bill is ${apples_price + bananas_price}.")

# Function calls
num_apples = get_fruits_count()
num_bananas = get_fruits_count()

apples_price = calculate_apples_price(num_apples)
bananas_price = calculate_bananas_price(num_bananas)

print_final_bill(apples_price, bananas_price)

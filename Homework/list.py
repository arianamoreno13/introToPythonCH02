#!/usr/bin/env python3

# ask the user to enter the number of values to be calculated.
def main():
    total_values = int(input("Enter the number of values to be calculated: "))
    numbers = []

# asks user to enter the numbers
    for i in range(total_values):
        number = float(input(f"Enter value {i+1}: "))
        numbers.append(number)

# calculates average of list
    average = sum(numbers) / total_values
    print("Average:", average)

# script is executed directly
if __name__ == "__main__":
    main()

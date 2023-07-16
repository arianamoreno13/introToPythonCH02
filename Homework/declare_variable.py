"""Module providingFunction printing python version."""
#Declare a variable and assign it the year you were born (or any number)
BIRTH_YEAR = 1997
#print the variable
print(BIRTH_YEAR)
#add 10 to the variable
BIRTH_YEAR = BIRTH_YEAR + 10
#print the variable
print(BIRTH_YEAR)
#subtract 100
BIRTH_YEAR = BIRTH_YEAR - 100
#print the variable
print(BIRTH_YEAR)
#multiply it by 2
BIRTH_YEAR = BIRTH_YEAR * 2
#print the variable
print(BIRTH_YEAR)

#Prompt the user for his/her name - use the input() function
FIRST_NAME = input("Enter your first name: ")
#assign the name to a variable & print
print(f"Hello, {FIRST_NAME}!")
#capitalize it
FIRST_NAME_CAP = FIRST_NAME.capitalize()
#print the variable
print(FIRST_NAME_CAP)
#remove any heading or trailing spaces
FIRST_NAME_CAP.lstrip().rstrip()
#print the variable
print(FIRST_NAME_CAP)

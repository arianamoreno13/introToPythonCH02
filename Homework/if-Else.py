"""Module providingFunction printing python version."""
#Write an if-else program prompts a user to enter a birth month.
#If the value entered is greater than 12 or less than 1, display an error message; otherwise, display the valid month.
BIRTH_MONTH = int(input("Please enter the month you were born."))
if BIRTH_MONTH == 1:
    MONTH = "January"
elif BIRTH_MONTH == 2:
    MONTH = "Febuary"
elif BIRTH_MONTH == 3:
    MONTH = "March"
elif BIRTH_MONTH == 4:
    MONTH = "April"
elif BIRTH_MONTH == 5:
    MONTH = "May"
elif BIRTH_MONTH == 6:
    MONTH = "June"
elif BIRTH_MONTH == 7:
    MONTH = "July"
elif BIRTH_MONTH == 8:
    MONTH = "August"
elif BIRTH_MONTH == 9:
    MONTH = "September"
elif BIRTH_MONTH == 10:
    MONTH = "October"
elif BIRTH_MONTH == 11:
    MONTH = "November"
elif BIRTH_MONTH == 12:
    MONTH = "December"
else:
    print("Birth month must be a number from 1-12")

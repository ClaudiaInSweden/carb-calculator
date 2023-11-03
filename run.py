""" 
Import libraries and connect to Google spreadsheets
"""
import gspread
from google.oauth2.service_account import Credentials
import webbrowser

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('carb-calculator')

compare = SHEET.worksheet('compare')

data = compare.get_all_values()

"""
Information for user what this project is about incl. instructions
"""
print("\nWelcome to the carbohydrate calculator for cat food!\n")
print("Most cat foods don't have the carb content listed but")
print("for people with obese and diabetic cats it's important to know")
print("how much carbs the food contains.\n") 
print("Use this interface to calculate the carb content of dry cat food.\n")
print("Please enter the respective percentage from your cat food label,")
print("using dot as decimal separator")
print("Example: Crude Protein/Protein in %: 12.5\n")

"""
Get food content data from user.
Five inputs need to be done. Inputs are converted to floats
and validated. A while loop runs until all five entered
values are valid.
"""

def get_user_input(var):
   
    while True:

        value = float(input("Enter {} in %: ".format(var)))
        try:
            if value > 99:
                raise ValueError
            elif value < 0:
                raise ValueError

        except ValueError as e:
            print(f"Value Error! Please enter a positive number between 0 and 100.\n")
            return False

        return True
        



protein = get_user_input("protein")
fat = get_user_input("fat")
fiber = get_user_input("fiber")
ash = get_user_input("ash")
moisture = get_user_input("moisture")

"""
We need the sum of the entered values to calculate the carb content
"""
subtotal = protein + fat + fiber + ash + moisture
"""
We calculate the carb content by subtracting the total of the 
entered values from 100 percent and print the result of the
calculation to the terminal.
"""
def calculate_carbs(subtotal):
    carbs = 100 - subtotal
    print(f"The cat food contains {carbs} % carbs.")
    return carbs

carb_result = calculate_carbs(subtotal)
food_content = [protein, fat, fiber, ash, moisture, carb_result]
print(food_content)

            
# Add data to excel sheet not yet created!!!

"""
Enable user to see the comparison of the entered items
"""
print("\nTo see the compilation of the cat food you entered, use (ctrl + click) to open the link:")

print('\033]8;;https://docs.google.com/spreadsheets/d/1nvKyRNOHlLlbLtARXVFYgILkAPpbYJ-Ywku7EwrQzts/edit?usp=sharing/\033\\Open the comparison\033]8;;\033\\\n')


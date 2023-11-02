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
Information for user what this project is about
"""

print("\nWelcome to the carbohydrate calculator for cat food!\n")
print("Most cat foods don't have the carb content listed but")
print("for people with obese and diabetic cats it's important to know")
print("how much carbs the food contains.\n") 
print("Use this interface to calculate the carb content of dry cat food.\n")
print("Please enter the respective percentage from your cat food label,")
print("using dot as decimal separator")
print("Example: Crude Protein/Protein in %: 12.5\n")



def get_user_input(var):
   
    while True:

        value = input("Enter {} in %: ".format(var))
        try:
            return float(value)
        except ValueError:
            print("Value Error! Please enter a valid number.\n")
            continue

protein = get_user_input("protein")
fat = get_user_input("fat")
fiber = get_user_input("fiber")
ash = get_user_input("ash")
moisture = get_user_input("moisture")

data = [protein, fat, fiber, ash, moisture]

print(data)
calculate_carbs()

def calculate_carbs():
    carbs = 100 - data
    print(f"The cat food contains {carbs} % carbs.")
    data.append(carbs)

print(data)

    
def user_choice_continue():

    while True:
        choice = input("Would you like to check another product? ( y / n ) : \n")
        if choice.casefold() == 'n':
            break
    calculate_carbs()
            
def main():
    get_user_input(var)
    calculate_carbs()
    user_choice_continue()  
    



"""
Enable user to see the comparison of the entered items
"""
print("\nTo see the compilation of the cat food you entered, use (ctrl + click) to open the link:")

print('\033]8;;https://docs.google.com/spreadsheets/d/1nvKyRNOHlLlbLtARXVFYgILkAPpbYJ-Ywku7EwrQzts/edit?usp=sharing/\033\\Open the comparison\033]8;;\033\\\n')


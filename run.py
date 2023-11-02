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


def get_user_input():
   
    print("\nWelcome to the carbohydrate calculator for cat food!\n")
    print("Most cat foods don't have the carb content listed but")
    print("for people with obese and diabetic cats it's important to know")
    print("how much carbs the food contains.\n") 
    print("Use this interface to calculate the carb content of dry cat food.\n")
    print("Please enter the respective percentage from your cat food label,")
    print("in the following order:\n")
    print("Protein, fat, fiber, ash, moisture (if there is no figure for moisture, take 8)\n,")
    print("Use a dot as decimal separator and a comma to separate the numbers.")
    print("Example: 37, 12, 6.1, 8.1, 8\n")

    while True:
        
        food_content = input("Enter percentages of protein, fat, fiber, ash and moisture as described above: \n")
        food_data = food_content.split(',')
        for i in range(len(food_data)):
            food_data[i] = float(food_data[i])
    return food_data
      
def validate_input(values):

    try:
        if len(values) != 5:
            raise ValueError(
                print("Please enter figures for protein, fat, fiber, ash and moisture!")
            )
    except ValueError as e:
        print("Value Error! Please enter a valid number.\n")
        return False
    except TypeError as e:
        print("Type Error! Please enter only numbers.\n")
        return False

    return True
                

def calculate_carbs():
    carbs = 100 - food_data
    print(f"The cat food contains {carbs} % carbs.")
    food_data.append(carbs)
    user_choice_continue()
    print(food_data)

def user_choice_continue():

    choice = input("Would you like to check another product? ( y / n ) : \n")
    if choice.casefold() == 'n':
        break
        
            
def main():
    get_user_input()
    validate_input(values)
    calculate_carbs()
    



"""
Enable user to see the comparison of the entered items
"""
print("To see the compilation of the cat food you entered, use (ctrl + click) to open the link:")

print('\033]8;;https://docs.google.com/spreadsheets/d/1nvKyRNOHlLlbLtARXVFYgILkAPpbYJ-Ywku7EwrQzts/edit?usp=sharing/\033\\Open the comparison\033]8;;\033\\\n')


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

print("Please enter the respective percentage from your cat food label with one decimal,")
print("using dot as decimal separator")
print("Example: Crude Protein/Protein in %: 12.5")

protein = float(input("Enter crude protein/protein in %:\n"))
fat = float(input("Enter crude fat/fat in %:\n"))
fiber = float(input("Enter crude fiber/fiber in %:\n"))
ash = float(input("Enter ash in %:\n"))
moisture = float(input("Enter moisture in %:\n"))
carbs = 100 - (protein + fat + fiber + ash + moisture)
print(carbs)





#
"""
Enable user to see the comparison of the entered items
"""
print("To see the compilation of the cat food you entered, use (ctrl + click) to open the link:")

print('\033]8;;https://docs.google.com/spreadsheets/d/1nvKyRNOHlLlbLtARXVFYgILkAPpbYJ-Ywku7EwrQzts/edit?usp=sharing/\033\\Open the comparison\033]8;;\033\\\n')
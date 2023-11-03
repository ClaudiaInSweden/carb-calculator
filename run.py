def display_instructions():
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

def get_user_input(var):
    """
    Get food content data from user.
    Five inputs need to be done. Inputs are converted to floats
    and validated. A while loop runs until all five entered
    values are valid.
    """
    while True:

        value = (input("Enter {} in %: \n".format(var)))
        try:
            return float(value)
            if 0 <= value >= 99:
                raise ValueError("Please enter a positive number between 0 and 100.")
        except ValueError as e:
            print("Value Error! Please enter a positive number between 0 and 100.\n")
            continue
           
def calculate_carbs(subtotal):
    """
    We calculate the carb content by subtracting the total of the 
    entered values from 100 percent and print the result of the
    calculation to the terminal.
    """
    carbs = 100 - subtotal
    print(f"\nThe cat food contains {carbs} % carbs.\n")
    return carbs

def calculate_carbs_in_cat_food():
    protein = get_user_input("protein")
    fat = get_user_input("fat")
    fiber = get_user_input("fiber")
    ash = get_user_input("ash")
    moisture = get_user_input("moisture")
    """
    We need the sum of the entered values to calculate the carb content
    """
    subtotal = protein + fat + fiber + ash + moisture
    carb_result = calculate_carbs(subtotal)
    food_content = [protein, fat, fiber, ash, moisture, carb_result]
    print(food_content)

if __name__ == '__main__':
    calculate_carbs_in_cat_food()
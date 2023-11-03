def display_instructions():
    """
    Information for user what this project is about incl. instructions
    about what kind of input is expected.
    """
    print("\n####################################################\n")
    print("Welcome to the carbohydrate calculator for cat food!\n")
    print("####################################################\n")
    print("Most dry food for cats doesn't have the carb content listed but")
    print("for people with obese and diabetic cats it's important to know")
    print("how much carbs the food contains.\n")
    print("Use this interface to calculate the carb content of cat food.\n")
    print("Please enter the respective percentage from your cat food label,")
    print("using dot as decimal separator and confirm with ENTER.\n")
    print("Example: Protein in %: 12.5\n")


def get_user_input(var):
    """
    Get food content data from user. Input labels are taken from
    variables defines in calculate_carbs_in_cat_food function.
    Five inputs need to be done. Inputs are converted to floats
    and validated. A while loop runs until all five entered
    values are valid.
    """
    while True:
        try:
            value = float(input("Enter {} in %: \n".format(var)))
            if 1 <= value <= 99:
                return value
            else:
                print("Please enter a number between 1 and 99.\n")
        except ValueError as e:
            print("Value Error! Please enter a number between 1 and 99.\n")
            continue


def calculate_carbs(subtotal):
    """
    We calculate the carb content by subtracting the total of the
    entered values from 100 percent and print the result of the
    calculation to the terminal.
    """
    carbs = 100 - subtotal
    carbs_rounded = round(carbs, 1)
    print(f"\nThe cat food contains {carbs_rounded} % carbs.\n")
    return carbs_rounded


def calculate_carbs_in_cat_food():
    """
    The following variables are taken as input from the user:
    """
    protein = get_user_input("protein")
    fat = get_user_input("fat")
    fiber = get_user_input("fiber")
    ash = get_user_input("ash")
    moisture = get_user_input("moisture")

    # We need the sum of the entered values to calculate the carb content
    subtotal = protein + fat + fiber + ash + moisture
    carb_result = calculate_carbs(subtotal)
    food_content = [protein, fat, fiber, ash, moisture, carb_result]

    print("\n#############################################################\n")
    print("Click on RUN PROGRAM on the top to calculate another product!")
    print("\n#############################################################\n")


if __name__ == '__main__':
    """
    Executes code when file runs as a script
    """
    display_instructions()
    calculate_carbs_in_cat_food()

# Task 2: Catering Choices

# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

food_choice = input("Would you like vegetarian food? Answer Yes or No: ")

if food_choice == 'Yes':
    action = print("We recommend Veggie Delight Caterers")
else:
    action = print("We recommend Gourmet Meals Caterer")

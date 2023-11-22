def generate_macro_needs_from_input(input_data):
    macro_needs = {}
    
    return macro_needs

def get_valid_meal_distribution():
    while True:
        breakfast_weight = float(input("Enter the percentage weight for Breakfast (0-1): "))
        lunch_weight = float(input("Enter the percentage weight for Lunch (0-1): "))
        dinner_weight = float(input("Enter the percentage weight for Dinner (0-1): "))
        
        if abs(breakfast_weight + lunch_weight + dinner_weight - 1.0) < 0.01:
            return {
                "Breakfast": breakfast_weight,
                "Lunch": lunch_weight,
                "Dinner": dinner_weight,
            }
        else:
            print("Sum of meal distribution percentages should be approximately 1.0. Please try again.")

def calculate_adjusted_macro_needs(macro_needs, meal_distribution):
    adjusted_macro_needs = {}
    
    for macro, value in macro_needs.items():
        adjusted_value = value / sum(meal_distribution.values())
        adjusted_macro_needs[macro] = {meal_type: adjusted_value * weight for meal_type, weight in meal_distribution.items()}
    
    return adjusted_macro_needs

"""
def display_menu(options):
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")
    
    while True:
        choice = input("Enter your choice: ")
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(options):
                return options[choice_idx]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
"""


"""
def generate_three_recipes(prompt, num_recipes):
    recipes = []
    
    for i in range(num_recipes):
        ingredient_list = input(f"Enter a comma-separated list of ingredients for recipe {i + 1} (or press Enter to skip): ").split(",")
        new_ingredient_list = f"\n\nIngredients: {', '.join(ingredient_list)}" if ingredient_list[0] else ""
        unique_prompt = f"{prompt} - Recipe {i + 1}{new_ingredient_list}"
        recipe = get_completion(unique_prompt)  # Assuming get_completion takes care of replacing the placeholders
        recipes.append(recipe)
    
    return recipes
"""




"""
breakfast_recipes = generate_three_recipes(generate_breakfast_meal_prompt(ingredient_list, adjusted_macro_needs, dietary_restrictions, allergies, food_restrictions), 3)
lunch_recipes = generate_three_recipes(generate_lunch_meal_prompt(ingredient_list, adjusted_macro_needs, dietary_restrictions, allergies, food_restrictions), 3)
dinner_recipes = generate_three_recipes(generate_dinner_meal_prompt(ingredient_list, adjusted_macro_needs, dietary_restrictions, allergies, food_restrictions), 3)
"""

"""
print("Breakfast Recipes:")
chosen_breakfast_recipe = display_menu(breakfast_recipes)
print(f"Chosen Breakfast Recipe:\n{chosen_breakfast_recipe}\n")

print("Lunch Recipes:")
chosen_lunch_recipe = display_menu(lunch_recipes)
print(f"Chosen Lunch Recipe:\n{chosen_lunch_recipe}\n")

print("Dinner Recipes:")
chosen_dinner_recipe = display_menu(dinner_recipes)
print(f"Chosen Dinner Recipe:\n{chosen_dinner_recipe}\n")
"""

#saving recipe 
def extracting_recipe_title(response):
    title = response.split("\n")[0]
    return title

def extract_ingredients(response):
    # Extract ingredients from the response
    ingredients_start = response.index("Ingredients:") + len("Ingredients:")
    ingredients_end = response.index("Instructions:")
    ingredients_text = response[ingredients_start:ingredients_end].strip()
    ingredients_list = [ingredient.strip() for ingredient in ingredients_text.split("\n") if ingredient]
    return ingredients_list

def extract_instructions(response):
    # Extract instructions from the response
    instructions_start = response.index("Instructions:") + len("Instructions:")
    serving_size_start = response.index("Serving Size:")
    instructions_text = response[instructions_start:serving_size_start].strip()
    return instructions_text

def extract_times(response):
    # Extract prep time and cook time from the response
    times_start = response.index("Prep time:")
    times_text = response[times_start:]
    
    prep_start = times_text.index(":") + 1
    prep_end = times_text.index("minutes", prep_start)
    prep_time = int(times_text[prep_start:prep_end].strip())
    
    cook_start = times_text.index("Cook time:") + len("Cook time:")
    cook_end = times_text.index("minutes", cook_start)
    cook_time_text = times_text[cook_start:cook_end].strip()
    
    # Handle cook time in range format
    if "-" in cook_time_text:
        # Split the range into start and end values
        cook_time_start, cook_time_end = map(int, cook_time_text.split("-"))
        # Calculate average of the range
        cook_time = (cook_time_start + cook_time_end) // 2
    else:
        cook_time = int(cook_time_text)
    
    return prep_time, cook_time

def extract_nutritional_info(response):
    # Find the starting index of the nutritional information section
    nutritional_info_start = response.index("Calorie Count:")
    # Extract the nutritional information section
    nutritional_info_text = response[nutritional_info_start:]

    # Extract individual nutritional values
    calorie_count = int(nutritional_info_text.split("Calorie Count:")[1].split("calories")[0].strip())
    fat_count = int(nutritional_info_text.split("Fat Count:")[1].split("g")[0].strip())
    protein_count = int(nutritional_info_text.split("Protein Count:")[1].split("g")[0].strip())
    saturated_fat_count = int(nutritional_info_text.split("Saturated Fat Count:")[1].split("g")[0].strip())
    sugar_count = int(nutritional_info_text.split("Sugar Count:")[1].split("g")[0].strip())
    carb_count = int(nutritional_info_text.split("Carb Count:")[1].split("g")[0].strip())

    # Return the extracted nutritional values
    return calorie_count, fat_count, protein_count, saturated_fat_count, sugar_count, carb_count



#ideas
#preset template 
#meal planner for a week
#advance prompt (chaining prompt togethers) (breaking it down into smaller subtasks) (break it down into each meal + breakfast)
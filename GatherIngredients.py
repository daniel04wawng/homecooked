from creat_recipe_event import main

def gather_ingredient_list(breakfast_ingredient_list, lunch_ingredient_list, dinner_ingredient_list, dietary_restrictions, allergies, food_restrictions, date_input, breakfast_time_input, lunch_time_input, dinner_time_input, input_data, meal_distribution, calendar_id):
    _, _, _, breakfast_list, lunch_list, dinner_list = main(breakfast_ingredient_list, lunch_ingredient_list, dinner_ingredient_list, dietary_restrictions, allergies, food_restrictions, date_input, breakfast_time_input, lunch_time_input, dinner_time_input, input_data, meal_distribution, calendar_id)
    
    # Combine the ingredient lists with counts
    combined_ingredients = {}
    
    for ingredient_list in [breakfast_list, lunch_list, dinner_list]:
        for ingredient in ingredient_list:
            ingredient_name, ingredient_count = ingredient.split(" (")  # Split ingredient name and count
            ingredient_name = ingredient_name.strip()  # Remove leading/trailing spaces
            ingredient_count = int(ingredient_count.rstrip("x)"))  # Remove 'x' and ')' and convert to int
            
            if ingredient_name in combined_ingredients:
                combined_ingredients[ingredient_name] += ingredient_count
            else:
                combined_ingredients[ingredient_name] = ingredient_count
    
    # Create the combined ingredient list with counts
    combined_ingredient_list = [f"{ingredient} ({count}x)" for ingredient, count in combined_ingredients.items()]
    
    # Print the combined ingredient list
    print(combined_ingredient_list)
    
    return combined_ingredient_list
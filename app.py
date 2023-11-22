from flask import Flask, render_template, request
from creat_recipe_event import main  
from nutrienttemplate import (
    foodenergy_template, protein_template, carbs_template,
    sugar_template, fat_template, saturated_fat_template,
    dietary_restrictions_template, allergies_template,
    food_exclusion_template
)

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html', 
                           foodenergy_template=foodenergy_template,
                           protein_template=protein_template,
                           carbs_template=carbs_template,
                           sugar_template=sugar_template,
                           fat_template=fat_template,
                           saturated_fat_template=saturated_fat_template,
                           dietary_restrictions_template=dietary_restrictions_template,
                           allergies_template=allergies_template,
                           food_exclusion_template=food_exclusion_template)

@app.route('/create_recipe', methods=['POST'])
def generate_recipe_page():
    print(request.form)
    
    calendar_id = request.form['calendar_id']
    breakfast_ingredient_list = request.form['breakfast_ingredient_list']
    lunch_ingredient_list = request.form['lunch_ingredient_list']
    dinner_ingredient_list = request.form['dinner_ingredient_list']
    date_input = request.form['date_input']
    breakfast_time_input = request.form['breakfast_time_input']
    lunch_time_input = request.form['lunch_time_input']
    dinner_time_input = request.form['dinner_time_input']
    use_template = request.form["use_template"]
    
    if use_template == "yes":
        input_data = {
            "Caloric Needs": 2425,
            "Protein Needs": 148,
            "Carbs Needs": 323,
            "Sugar Needs": 65,
            "Fat Needs": 69,
            "Saturated Fat Needs": 28,
        }
    else:
        caloric_needs = int(request.form['caloric_needs'])
        protein_needs = int(request.form['protein_needs'])
        carbs_needs = int(request.form['carbs_needs'])
        sugar_needs = int(request.form['sugar_needs'])
        fat_needs = int(request.form['fat_needs'])
        saturated_fat_needs = int(request.form['saturated_fat_needs'])
    
        input_data = {
            "Caloric Needs": caloric_needs,
            "Protein Needs": protein_needs,
            "Carbs Needs": carbs_needs,
            "Sugar Needs": sugar_needs,
            "Fat Needs": fat_needs,
            "Saturated Fat Needs": saturated_fat_needs,
        }

    dietary_restrictions = request.form.getlist('dietary_restrictions')
    allergies = request.form.getlist('allergies')
    food_restrictions = request.form['food_restrictions']

    meal_distribution = {
        "breakfast_weight": float(request.form['breakfast_weight']),
        "lunch_weight": float(request.form['lunch_weight']),
        "dinner_weight": float(request.form['dinner_weight']),
    }
    # Call your backend code here to generate the recipes and get the links
    breakfast_link, lunch_link, dinner_link = main(breakfast_ingredient_list, lunch_ingredient_list, dinner_ingredient_list ,dietary_restrictions, allergies, food_restrictions, date_input, breakfast_time_input, lunch_time_input,dinner_time_input, input_data, meal_distribution, calendar_id)




    return render_template('index.html', 
                           breakfast_link=breakfast_link, 
                           lunch_link=lunch_link, 
                           dinner_link=dinner_link)

if __name__ == '__main__':
    app.run(debug=True)
    
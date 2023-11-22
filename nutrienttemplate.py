def foodenergy_template():
    caloric_needs = input("Enter your caloric needs: ")
    template = f'''
    <label for="caloric_needs">Caloric Needs:</label>
    <input type="number" name="caloric_needs" value="{caloric_needs}" required><br><br>
    '''
    return template

def protein_template():
    protein_needs = input("Enter your protein needs: ")
    template = f'''
    <label for="protein_needs">Protein Needs:</label>
    <input type="number" name="protein_needs" value="{protein_needs}" required><br><br>
    '''
    return template

def carbs_template():
    carbs_needs = input("Enter your carbs needs: ")
    template = f'''
    <label for="carbs_needs">Carbs Needs:</label>
    <input type="number" name="carbs_needs" value="{carbs_needs}" required><br><br>
    '''
    return template

def sugar_template():
    sugar_needs = input("Enter your sugar needs: ")
    template = f'''
    <label for="sugar_needs">Sugar Needs:</label>
    <input type="number" name="sugar_needs" value="{sugar_needs}" required><br><br>
    '''
    return template

def fat_template():
    fat_needs = input("Enter your fat needs: ")
    template = f'''
    <label for="fat_needs">Fat Needs:</label>
    <input type="number" name="fat_needs" value="{fat_needs}" required><br><br>
    '''
    return template

def saturated_fat_template():
    saturated_fat_needs = input("Enter your saturated fat needs: ")
    template = f'''
    <label for="saturated_fat_needs">Saturated Fat Needs:</label>
    <input type="number" name="saturated_fat_needs" value="{saturated_fat_needs}" required><br><br>
    '''
    return template

def dietary_restrictions_template():
    return '''
    <label for="dietary_restrictions">Dietary Restrictions:</label><br>
    <input type="checkbox" name="dietary_restrictions" value="vegetarian"> Vegetarian<br>
    <input type="checkbox" name="dietary_restrictions" value="vegan"> Vegan<br>
    <input type="checkbox" name="dietary_restrictions" value="gluten-free"> Gluten-Free<br>
    <input type="checkbox" name="dietary_restrictions" value="dairy-free"> Dairy-Free<br>
    '''

def allergies_template():
    return '''
    <label for="allergies">Allergies:</label><br>
    <input type="checkbox" name="allergies" value="nuts"> Nuts<br>
    <input type="checkbox" name="allergies" value="shellfish"> Shellfish<br>
    <input type="checkbox" name="allergies" value="soy"> Soy<br>
    <input type="checkbox" name="allergies" value="wheat"> Wheat<br>
    '''

def food_exclusion_template():
    return '''
    <label for="food_exclusions">Excluded Foods:</label><br>
    <input type="text" name="food_exclusions" placeholder="Enter excluded foods, separated by commas"><br><br>
    '''


from __future__ import print_function

from OpenAI import calculate_adjusted_macro_needs, extract_ingredients, extract_instructions, extract_times, extracting_recipe_title, extract_nutritional_info

from prompts import get_completion, generate_breakfast_meal_prompt, generate_lunch_meal_prompt, generate_dinner_meal_prompt


from datetime import datetime 
from datetime import timedelta
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os

print("Current working directory: ", os.getcwd())

# If modifying these scopes, delete the file token.json.

SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def create_event(service, start_datetime, title, ingredients_list, instructions_text, prep_time, cook_time, calorie_count, fat_count, protein_count, saturated_fat_count, sugar_count, carb_count, calendar_id):
    event = {
        'summary': title,
        'description': (
            "Ingredients:\n" + '\n'.join(ingredients_list) +
            "\n\nInstructions:\n" + instructions_text +
            f"\n\nNutritional Info:\nCalorie Count: {calorie_count}\nFat count: {fat_count}g\nProtein count: {protein_count}g\nSaturated fat count: {saturated_fat_count}g\nSugar count: {sugar_count}g\nCarb count: {carb_count}g"
        ),
        'start': {
            'dateTime': start_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'UTC-7',
        },
        'end': {
            'dateTime': (start_datetime + timedelta(minutes=(prep_time + cook_time))).strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'UTC-7',
        }
    }
    created_event = service.events().insert(calendarId=calendar_id, body=event).execute()
    print('Event created: %s' % created_event.get('htmlLink'))




def main(breakfast_ingredient_list, lunch_ingredient_list, dinner_ingredient_list ,dietary_restrictions, allergies, food_restrictions, date_input, breakfast_time_input, lunch_time_input,dinner_time_input, input_data, meal_distribution, calendar_id):
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES
        )
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    adjusted_macro_needs = calculate_adjusted_macro_needs(input_data, meal_distribution)
    
    try:
        print("Before building service")
        service = build('calendar', 'v3', credentials=creds)
        print("Service built.")
        
        # user input
        breakfast_prompt = generate_breakfast_meal_prompt(breakfast_ingredient_list, adjusted_macro_needs, dietary_restrictions, allergies, food_restrictions)
        breakfast_response = get_completion(breakfast_prompt, model="gpt-3.5-turbo")
        breakfast_title = extracting_recipe_title(breakfast_response)
        breakfast_ingredients_list = extract_ingredients(breakfast_response)
        breakfast_instructions_text = extract_instructions(breakfast_response)
        breakfast_prep_time, breakfast_cook_time = extract_times(breakfast_response)
        valid_date = datetime.strptime(date_input, '%Y-%m-%d').date()  # Parse date input
        breakfast_valid_time = datetime.strptime(breakfast_time_input, '%H:%M').time()
        breakfast_start_datetime = datetime.combine(valid_date, breakfast_valid_time)
        breakfast_calorie_count, breakfast_fat_count, breakfast_protein_count, breakfast_saturated_fat_count, breakfast_sugar_count, breakfast_carb_count, = extract_nutritional_info(breakfast_response)
        # Call the create_event function to create an event
        create_event(service, breakfast_start_datetime, breakfast_title, breakfast_ingredients_list , breakfast_instructions_text, breakfast_prep_time, breakfast_cook_time, breakfast_calorie_count, breakfast_fat_count, breakfast_protein_count, breakfast_saturated_fat_count, breakfast_sugar_count, breakfast_carb_count, calendar_id)
        breakfast_calendar_link = f"https://calendar.google.com/calendar/r/eventedit?text={breakfast_title}&details={breakfast_instructions_text}&dates={(breakfast_start_datetime).strftime('%Y%m%dT%H%M%S')}%2F{(breakfast_start_datetime + timedelta(minutes=(breakfast_prep_time + breakfast_cook_time))).strftime('%Y%m%dT%H%M%S')}"
        
        lunch_prompt = generate_lunch_meal_prompt(lunch_ingredient_list, adjusted_macro_needs, dietary_restrictions, allergies, food_restrictions)
        lunch_response = get_completion(lunch_prompt, model="gpt-3.5-turbo")
        print (lunch_response)
        lunch_title = extracting_recipe_title(lunch_response)
        lunch_ingredients_list = extract_ingredients(lunch_response)
        lunch_instructions_text = extract_instructions(lunch_response)
        lunch_prep_time, lunch_cook_time = extract_times(lunch_response)
        valid_date = datetime.strptime(date_input, '%Y-%m-%d').date()  # Parse date input
        lunch_valid_time = datetime.strptime(lunch_time_input, '%H:%M').time()
        lunch_start_datetime = datetime.combine(valid_date, lunch_valid_time)
        lunch_calorie_count, lunch_fat_count, lunch_protein_count, lunch_saturated_fat_count, lunch_sugar_count, lunch_carb_count, = extract_nutritional_info(lunch_response)
        # Call the create_event function to create an event
        create_event(service, lunch_start_datetime, lunch_title, lunch_ingredients_list, lunch_instructions_text, lunch_prep_time, lunch_cook_time, lunch_calorie_count, lunch_fat_count, lunch_protein_count, lunch_saturated_fat_count, lunch_sugar_count, lunch_carb_count, calendar_id)
        lunch_calendar_link = f"https://calendar.google.com/calendar/r/eventedit?text={lunch_title}&details={lunch_instructions_text}&dates={(lunch_start_datetime).strftime('%Y%m%dT%H%M%S')}%2F{(lunch_start_datetime + timedelta(minutes=(lunch_prep_time + lunch_cook_time))).strftime('%Y%m%dT%H%M%S')}"

        dinner_prompt = generate_dinner_meal_prompt(dinner_ingredient_list, adjusted_macro_needs, dietary_restrictions, allergies, food_restrictions)
        dinner_response = get_completion(dinner_prompt, model="gpt-3.5-turbo")
        print (dinner_response)
        dinner_title = extracting_recipe_title(dinner_response)
        dinner_ingredients_list = extract_ingredients(dinner_response)
        dinner_instructions_text = extract_instructions(dinner_response)
        dinner_prep_time, dinner_cook_time = extract_times(dinner_response)
        valid_date = datetime.strptime(date_input, '%Y-%m-%d').date()  # Parse date input
        dinner_valid_time = datetime.strptime(dinner_time_input, '%H:%M').time()
        dinner_start_datetime = datetime.combine(valid_date, dinner_valid_time)
        dinner_calorie_count, dinner_fat_count, dinner_protein_count, dinner_saturated_fat_count, dinner_sugar_count, dinner_carb_count, = extract_nutritional_info(dinner_response)
        # Call the create_event function to create an event
        create_event(service, dinner_start_datetime, dinner_title, dinner_ingredients_list, dinner_instructions_text, dinner_prep_time, dinner_cook_time, dinner_calorie_count, dinner_fat_count, dinner_protein_count, dinner_saturated_fat_count, dinner_sugar_count, dinner_carb_count, calendar_id)
        dinner_calendar_link = f"https://calendar.google.com/calendar/r/eventedit?text={dinner_title}&details={dinner_instructions_text}&dates={(dinner_start_datetime).strftime('%Y%m%dT%H%M%S')}%2F{(dinner_start_datetime + timedelta(minutes=(dinner_prep_time + dinner_cook_time))).strftime('%Y%m%dT%H%M%S')}"

        return breakfast_calendar_link, lunch_calendar_link, dinner_calendar_link, 
    
    except HttpError as error:
        print('An error occurred: %s' % error)




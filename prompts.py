import openai

import os

import pandas as pd

import time

import datetime

openai.api_key = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    # Access the content within the message object
    return response.choices[0].message['content']

def generate_breakfast_meal_prompt(breakfast_ingredient_list, macro_needs, dietary_restrictions, allergies, food_restrictions):
    prompt = f"""
    
Give me the best breakfast recipe using {", ".join(breakfast_ingredient_list)}  and other ingredients based on your choosing for breakfast

Note: If {", ".join(breakfast_ingredient_list)} = Nothing , give me the best recipe for a healthy, hearty, and yummy breakfast

Note: when creating the recipe, make sure to say how long the prep time and cooking time would be at the end

Note: put the title of the recipe at the beginning without having title of the recipe: 

Note: when generating meal, keep into account the dietary restrictions: {dietary_restrictions} and allergies: {allergies} and any food restrictions:
 {food_restrictions}

Note: take into account {macro_needs} when designing these meals; they do not need to be exact but keep it around the same

For example

Note: make these meals as diverse and specific as possible based on the specified {macro_needs} while ensuring that they are the best and yummiest

Note: when constructing these recipes, if the meal is lacking in protein, vitamins, or carbs, add side dishes to the original recipe and put it together into

Structure:

Title of the Recipe (Please bold the title of the recipe):

Ingredients: 
1. 
2.
3.

Note: When listing off ingredients, be specific with the amount of ingredient used, type of cut of protein (such as specific fish, pork cuts, etc, make sure to only choose one specific cut), serving amounts, etc

Instructions
1.
2.
3.

Serving Size:
Prep time:
Cook time:

Calorie Count: 
Fat Count:
Protein Count:
Saturated Fat Count:
Sugar Count:
Carb Count: 

"""
    return prompt

def generate_lunch_meal_prompt(lunch_ingredient_list,macro_needs, dietary_restrictions, allergies, food_restrictions):
    prompt = f"""
    
Give me the best lunch recipe using {", ".join(lunch_ingredient_list)}  and other ingredients based on your choosing for lunch

Note: If {", ".join(lunch_ingredient_list)} = Nothing or its empty, give me the best recipe for a healthy, hearty, and yummy lunch

Note: when creating the recipe, make sure to say how long the prep time and cooking time would be at the end

Note: put the title of the recipe at the beginning without having title of the recipe: 

Note: when generating meal, keep into account the dietary restrictions: {dietary_restrictions} and allergies: {allergies} and any food restrictions:
 {food_restrictions}

Note: take into account {macro_needs} when designing these meals; they do not need to be exact but keep it around the same

Note: make these meals as diverse and specific as possible based on the specified {macro_needs} while ensuring that they are the best and yummiest

Note: when constructing these recipes, if the meal is lacking in protein, vitamins, or carbs, add side dishes to the original recipe and put it together into

Structure:

Title of the Recipe (Please bold the title of the recipe):

Ingredients: 
1. 
2.
3.

Note: When listing off ingredients, be specific with the amount of ingredient used, type of cut of protein (such as specific fish, pork cuts, etc, make sure to only choose one specific cut), serving amounts, etc

Instructions
1.
2.
3.

Serving Size:
Prep time:
Cook time:

Calorie Count: 
Fat Count:
Protein Count:
Saturated Fat Count:
Sugar Count:
Carb Count: 

"""
    return prompt

def generate_dinner_meal_prompt(dinner_ingredient_list, macro_needs, dietary_restrictions, allergies, food_restrictions):
    prompt = f"""
    
Give me the best dinner recipe using {", ".join(dinner_ingredient_list)}  and other ingredients based on your choosing for dinner

Note: If {", ".join(dinner_ingredient_list)} = Nothing of empty, give me the best recipe for a healthy, hearty, and yummy dinner

Note: when creating the recipe, make sure to say how long the prep time and cooking time would be at the end

Note: put the title of the recipe at the beginning without having title of the recipe: 

Note: when generating meal, keep into account the dietary restrictions: {dietary_restrictions} and allergies: {allergies} and any food restrictions:
 {food_restrictions}

Note: take into account {macro_needs} when designing these meals; they do not need to be exact but keep it around the same

Note: make these meals as diverse and specific as possible based on the specified {macro_needs} while ensuring that they are the best and yummiest

Note: when constructing these recipes, if the meal is lacking in protein, vitamins, or carbs, add side dishes to the original recipe and put it together into

Structure:

Title of the Recipe (Please bold the title of the recipe):

Ingredients: 
1. 
2.
3.

Note: When listing off ingredients, be specific with the amount of ingredient used, type of cut of protein (such as specific fish, pork cuts, etc, make sure to only choose one specific cut), serving amounts, etc

Instructions
1.
2.
3.

Serving Size:
Prep time (x minutes):
Cook time (x minutes):

Calorie Count: 
Fat Count:
Protein Count:
Saturated Fat Count:
Sugar Count:
Carb Count: 

Example Recipe:
Baked Salmon with Grapefruit Salad
Ingredients
1. 1 (¾ pound) salmon filet
2. ½ teaspoon sea salt
3. Freshly cracked black pepper, to taste
4. 4 cups spring mix salad greens
5. 1 avocado, cubed
6. 1 large grapefruit
7.Honey Mustard Vinaigrette, for serving
8. Lemon wedges, for serving


Instructions:
1. Preheat the oven to 350°F with a rack in the center position. Line a rimmed sheet pan with parchment paper.
2. Place the salmon on the prepared sheet pan and sprinkle with salt and pepper to taste.
3. Bake until the fish easily flakes with a fork, about 12 to 15 minutes (depending on thickness).
4. Meanwhile make the salad. Using a small paring knife, trim the tops and bottoms off the grapefruit so they sit flat. Carefully trim the peel off just enough to expose the fruit while removing as much of the white pith as possible. From here, either supreme the fruit by cutting out each wedge from the membranes or slicing into rounds.
5. Divide the salad greens onto 4 plates. Top with avocado and grapefruit. Drizzle with the vinaigrette. Divide the salmon into two pieces, discard the skin and place one piece on top of each salad.
6. Serve with lemon wedges alongside.

Serving Size: 2
Prep time: 15 minutes
Cook time: 15 minutes

Calorie Count: 557 calories per serving
Fat Count: 24g per serving
Protein Count: 52g per serving
Saturated Fat Count: 2g per serving
Sugar Count: 7g per serving
Carb Count: 33g per serving
"""
    return prompt
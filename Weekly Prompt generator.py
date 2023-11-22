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

    return response.choices[0].message["content"]

def weekly_generate_recipe(ingredient, cost, type_of_meal, dietary_restrictions, allegies, food_exclusions):
    prompt = f"""
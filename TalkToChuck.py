import random

import requests
import os

RAPID_API_KEY = os.getenv('RAPID_API_KEY')


def get_categories():
	"""
	Get Chuck Norris categories
	:return: list of categories
	"""
	url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/categories"

	headers = {
		"accept": "application/json",
		"X-RapidAPI-Key": RAPID_API_KEY,
		"X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers)

	categories = response.json()

	return categories


def get_joke(category=""):
	"""
	Get a Chuck Norris joke
	:param category: category to pull joke from or use random category
	:return: json object with joke
	"""
	if category:
		category_query = {"category": category}
	else:
		category_query = ""

	url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

	headers = {
		"accept": "application/json",
		"X-RapidAPI-Key": RAPID_API_KEY,
		"X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=category_query)

	return response.json()


def get_random_joke():
	"""
	Generate a random joke by passing in a random category
	:return: dictionary object with joke
	"""

	categories = get_categories()
	num_categories = len(categories)
	random_int = random.randint(0, num_categories)
	random_category = categories[random_int]

	random_joke = get_joke(random_category)

	return random_joke


if __name__ == '__main__':
	joke = get_random_joke()
	print(joke)

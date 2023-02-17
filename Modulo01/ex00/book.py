# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdasilva <jdasilva@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/17 11:43:22 by jdasilva          #+#    #+#              #
#    Updated: 2023/02/17 17:33:01 by jdasilva         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import date
from recipe import Recipe

class Book:
	def __init__(self, name, last_update = None, creation_date = None, recipe_list = None):
		if not isinstance(name, str):
			raise TypeError("Name Error")
		self.name = name
		self.last_update = last_update if last_update is not None else date.today()
		self.creation_date = creation_date if creation_date is not None else date.today()
		self.recipe_list = recipe_list if recipe_list is not None else {"starter":[], "lunch":[], "dessert":[]}

	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""
		for recipe_name in self.recipe_list:
			for recipe in self.recipe_list[recipe_name]:
				if recipe.name == name:
					print(recipe)
					return 0			
		return print("Error Recipe not found")
	
	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		for i in self.recipe_list[recipe_type]:
			print(i.name)
	
	def add_recipe(self, recipe):
		"""Add a recipe to the book and update"""
		if not isinstance(recipe, Recipe):
			print("This recipe doesn't exist")
		else:
			self.recipe_list[recipe.recipe_type].append(recipe)

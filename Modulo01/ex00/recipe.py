# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdasilva <jdasilva@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/17 11:43:24 by jdasilva          #+#    #+#              #
#    Updated: 2023/02/17 16:17:03 by jdasilva         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        
        if not isinstance(name, str) or not isinstance(description, str):
            raise TypeError("Type Error")
        if not isinstance(cooking_lvl, int) or cooking_lvl < 1 or cooking_lvl > 5:
            raise ValueError("Type Error Cooking_lvl Range Error")
        if not isinstance(cooking_time, int) or cooking_time < 0:
            raise ValueError("Type Error Cooking_item should not be negative.")
        if not all(isinstance(i, str) for i in ingredients):
            raise TypeError("Ingredient List Error")
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise TypeError("Recipe type must be 'starter', 'lunch' or 'dessert'")
      
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        
    def __str__(self):
        return f"{self.name} ({self.recipe_type}, level: {self.cooking_lvl}, {self.cooking_time} min)"
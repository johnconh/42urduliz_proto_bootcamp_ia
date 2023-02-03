# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdasilva <jdasilva@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 16:44:01 by jdasilva          #+#    #+#              #
#    Updated: 2023/02/03 18:13:40 by jdasilva         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

Sandwich = {
    "ingredients": ["han", "breab", "cheese", "tomatoes"],
    "meal": "lunch",
    "prep_time": 10
}

Cake = {
    "ingredients": ["flour", "sugar", "eggs"],
    "meal": "dessert",
    "prep_time": 60
}

Salad = {
    "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
    "meal": "lunch",
    "prep_time": 15
}

cookbook = {
    "Sandwich" : Sandwich,
    "Cake" : Cake,
    "Salad" : Salad,
}

def print_all_names(dic):
    for key in dic:
        print(key)
        
def print_details(str, dic):
    for key in dic:
        if key == str:
            print(dic[key])
            return
        
def delete_recipe(str, dic):
    for key in dic:
        if key == str:
            del dic[key]
            return

def add_recipe(dic):
    name = input(">>> Enter a name:\n")
    print(">>> Enter a ingredient:")
    ingredient = []
    ing = input()
    while ing != "":
        ingredient.append(ing)
        ing = input()
    meal = input(">>> Enter a seal type:\n")
    prep_time = input(">>> Enter a preparation time:\n")
    
    recipe ={
        "ingredients": ingredient,
        "meal" : meal,
        "prep_time": prep_time,
	}
    cookbook[name] = recipe
add_recipe(cookbook)
#print_details("tortilla", dic)
#print(cookbook)
print_all_names(cookbook)
    
    
                        
                        
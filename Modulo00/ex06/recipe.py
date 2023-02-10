# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdasilva <jdasilva@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 16:44:01 by jdasilva          #+#    #+#              #
#    Updated: 2023/02/10 12:33:19 by jdasilva         ###   ########.fr        #
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

    if dic.get(str) == None:
            return (print("Sorry, this option does not exist."))
    print(
        f"""
Recipe for {str}:
    Ingredients list: {dic[str]['ingredients']}
    To be eaten for {dic[str]['meal']}.
    Takes {dic[str]['prep_time']} minutes of cooking. 
        """)
#   cont = 0
#   for name, value in dic[str].items():
#       print(name, end = " ")
#       if cont == 0:
#           print(*value, sep=", ")
#       else:
#           print(value)
#        cont += 1 """
        
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

def main():
    while True:
        print( """
Welcome to the Python Cookbook !
List of available option:
    1: Add a recipe
    2: Delete a recipe
    3: Print a recipe
    4: Print the cookbook
    5: Quit
            
        """
        )
        option = input("Please select an option:\n>> ")
                
        if option == '1':
            add_recipe()
        elif option == '2':
            delete_recipe()
        elif option == '3':
            recipe = input("Please enter a recipe name to get its details:\n")
            print_details(recipe, cookbook)
        elif option == '4':
            print_all_names(cookbook)
        elif option == '5':
            break
        else:
            print("Sorry, this option does not exist.")

if __name__=="__main__":
    main()                
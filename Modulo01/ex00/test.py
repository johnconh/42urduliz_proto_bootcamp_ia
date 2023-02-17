# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdasilva <jdasilva@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/17 11:43:27 by jdasilva          #+#    #+#              #
#    Updated: 2023/02/17 17:31:45 by jdasilva         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

## Crear un objeto Book
libro = Book("Libro de recetas")

# Crear un objeto Recipe y agregarlo al libro
tortilla = Recipe("tortilla", 2, 2, ["huevos", "aceite", "patatas", "cebolla"], "Tortila de cebolla", recipe_type="lunch")
Ensalada = Recipe("Ensalada de frutas", 3, 10, ["manzanas", "naranjas", "plátanos"], "Una deliciosa ensalada de frutas.", recipe_type="dessert")
libro.add_recipe(tortilla)
libro.add_recipe(Ensalada)
# Obtener una receta por su nombre
libro.get_recipe_by_name("tortilla")

# Agregar una receta no válida (una cadena en lugar de un objeto Recipe)
libro.add_recipe("no vale")

# Obtener todas las recetas de un tipo específico
libro.get_recipes_by_types("dessert")


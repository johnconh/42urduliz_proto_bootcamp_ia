# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdasilva <jdasilva@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 10:30:17 by jdasilva          #+#    #+#              #
#    Updated: 2023/02/03 17:39:44 by jdasilva         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def text_analyzer(text=None):
	"""
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text."""
	
	if text == None:
		text = input("What is the text to analyze?\n")
	if text.isnumeric():
		print("AssertionError: argument is not a string")
		return
	mayusculas = 0
	minusculas = 0
	espacios = 0
	signos = 0
	total = 0
	for char in text:
		total +=1
		if char.isupper():
			mayusculas += 1
		elif char.islower():
			minusculas += 1
		elif char.isspace():
			espacios += 1
		elif char in string.punctuation:
			signos += 1
	print("The text contains", total, "character(s):")
	print("-", mayusculas, "upper letter(s)")
	print("-", minusculas, "lower letter(s)")
	print("-", signos, "puntuaction mark(s)")
	print("-", espacios, "space(s)")
	
if __name__=="__main__":
	
	if len(sys.argv) > 2:
		sys.exit(print("Error: demasiados argumentos"))
	elif len(sys.argv) == 2:
		text_analyzer(sys.argv[1])
	else:
		text_analyzer()
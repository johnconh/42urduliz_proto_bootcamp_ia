# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdasilva <jdasilva@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/03 11:29:32 by jdasilva          #+#    #+#              #
#    Updated: 2023/03/03 12:44:43 by jdasilva         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def generator(text, sep=" ", option=None):
	'''
	Splits the text according to sep value and yield the substrings.
	Option precise if a action is performed to the substrings before it is yielded.
	'''
	if not isinstance(text, str):
		raise TypeError("ERROR")
	words = text.split(sep)
	if option not in [None, "shuffle", "unique", "ordered"]:
		raise ValueError("ERROR")
	if option == "shuffle":
		for i in range(len(words) -1, 0, -1):
			j = random.randint(0, i)
			words[i], words[j] = words[j], words[i]
	if option == "unique":
		words = list(set(words))
	if option == "ordered":
		words = sorted(words)
	for word in words:
		yield word
	
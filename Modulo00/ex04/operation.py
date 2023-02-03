# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operation.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdasilva <jdasilva@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 13:07:03 by jdasilva          #+#    #+#              #
#    Updated: 2023/02/03 14:15:51 by jdasilva         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 3:
	if sys.argv[1].isnumeric() and sys.argv[2].isnumeric():
		num1 = int(sys.argv[1])
		num2 = int(sys.argv[2])
		print("Sum: ", num1 + num2)
		print("Diferencie:", num1 - num2)
		print("Product:", num1 * num2)
		try:
			print("Quotient:", num1 / num2)
		except:
			print("Quotient: ERROR (division by zero)")
		try:	
			print("Remainder:", num1 % num2)
		except:
			print("Remainder: ERROR (modulo by zero)")
	else:
		print("AssertionError: only integers")
else:
	print("AssertionError: too many arguments")
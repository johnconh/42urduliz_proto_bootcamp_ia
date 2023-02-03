# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdasilva <jdasilva@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 09:48:35 by jdasilva          #+#    #+#              #
#    Updated: 2023/02/03 13:10:51 by jdasilva         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 2:
	sys.exit(print("Error: demasiados argumentos"))  
try:
    num = int(sys.argv[1])
except IndexError:
	sys.exit()
except ValueError:
      sys.exit(print("Error: no es un numero entero"))
      
if num == 0:
    print ("Zero") 
elif num % 2 == 0:
    print("🖕par")
else:
	print("🤘impar")
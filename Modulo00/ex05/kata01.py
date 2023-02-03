# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdasilva <jdasilva@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/03 15:53:38 by jdasilva          #+#    #+#              #
#    Updated: 2023/02/03 15:59:17 by jdasilva         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = {
    'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
	}

for key, values in kata.items():
	print(f"{key} was created {values}")
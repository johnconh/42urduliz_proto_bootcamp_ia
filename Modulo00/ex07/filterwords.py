# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdasilva <jdasilva@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/10 12:34:24 by jdasilva          #+#    #+#              #
#    Updated: 2023/02/10 13:27:10 by jdasilva         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

if len(sys.argv) != 3 or type (sys.argv[1]) is not str or sys.argv[2].isnumeric == False:
	exit(print("Error"))

S = sys.argv[1]
N = sys.argv[2]

S = S.translate(str.maketrans("", "", string.punctuation))
S = S.split()
Words = []
for str in S:
	if(len(str) > int(N)):
		Words.append(str)
print(Words)
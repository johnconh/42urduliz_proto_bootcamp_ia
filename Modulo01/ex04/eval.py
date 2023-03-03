# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdasilva <jdasilva@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/03 12:33:10 by jdasilva          #+#    #+#              #
#    Updated: 2023/03/03 13:05:28 by jdasilva         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Evaluator:
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        return sum(coef * len(word) for coef, word in zip(coefs, words))
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        return sum(coefs[i] * len(words[i]) for i in range(len(words)))

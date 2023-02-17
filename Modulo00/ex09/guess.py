# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdasilva <jdasilva@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/17 11:01:43 by jdasilva          #+#    #+#              #
#    Updated: 2023/02/17 11:38:29 by jdasilva         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
	
def main():
    """
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
    """
    numero_secreto = random.randint(1, 99)
    intentos = 0
    while True:
        text = input("What's your guess between 1 and 99?\n>>")
        if text.lower() == "exit":
               return(print("Goodbye!"))
        try:
             numero = int(text)
        except ValueError:
             print("That's not a number.")
             continue
        intentos += 1
        if numero == numero_secreto:
            print("Congratulations, you've got it!")
            if intentos == 1:
                   print("Congratulations! You got it on your first try!")
            else:
                 print(f"You won in {intentos} attempts!")
            return
        elif numero > numero_secreto:
             print("Too high!")
        else:
             print("Too low!")
    	
if __name__=="__main__":
   print(main.__doc__)
   main()
    
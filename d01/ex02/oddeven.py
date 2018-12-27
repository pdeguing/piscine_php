# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    oddeven.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdeguing <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/27 10:33:12 by pdeguing          #+#    #+#              #
#    Updated: 2018/12/27 11:09:15 by pdeguing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if __name__ == '__main__':
    while True:
        try:
            str = input('Entrez un nombre: ')
        except EOFError:
            print ("\n", end='')
            break
        if str.isnumeric() == False:
            print(str, "n'est pas un chiffre")
        else:
            number = int(str)
            print("Le chiffre", number, "est", end=" ")
            if number % 2:
                print("Impair")
            else:
                print("Pair")

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    do_op.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdeguing <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/27 15:29:02 by pdeguing          #+#    #+#              #
#    Updated: 2018/12/27 16:14:59 by pdeguing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def do_op(av):
    if len(av) != 2:
        print("Incorrect Parameters")
        return
    try:
        print(eval(' '.join(av[1:])))
    except:
        print("Syntax Error")

if __name__ == "__main__":
    do_op(sys.argv)

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    do_op.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdeguing <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/27 15:29:02 by pdeguing          #+#    #+#              #
#    Updated: 2018/12/27 15:52:29 by pdeguing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def do_op(av):
    if len(av) != 4:
        print("Incorrect Parameters")
        return
    print(eval(' '.join(av[1:])))

if __name__ == "__main__":
    do_op(sys.argv)

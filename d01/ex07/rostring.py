# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    rostring.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdeguing <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/27 12:39:34 by pdeguing          #+#    #+#              #
#    Updated: 2018/12/27 14:21:11 by pdeguing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def rostring(av):
    if len(av) < 2:
        return
    words = av[1].split()
    if len(words) > 1:
        print(' '.join(words[1:]), words[0])
    elif len(words) == 1:
        print(words[0])

if __name__ == "__main__":
    rostring(sys.argv)

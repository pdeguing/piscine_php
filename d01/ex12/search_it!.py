# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    search_it!.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pdeguing <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/12/27 16:16:01 by pdeguing          #+#    #+#              #
#    Updated: 2018/12/27 16:40:49 by pdeguing         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def search_it(av):
    if len(av) < 3:
        return
    key = av[1]
    dict1 = dict(word.split(':') for word in av[2:]) 
    if key in dict1:
        print(dict1.get(key))

if __name__ == "__main__":
    search_it(sys.argv)
